import torch
from transformers import VitsModel, AutoTokenizer
from vocoder_inference import load_hifi_gan_vocoder, mel_to_audio, save_audio

def infer_tts(text, model, tokenizer, hifi_gan, output_wav_path="output.wav", sampling_rate=22050):
    # 텍스트를 토큰화하고 Mel-spectrogram 생성
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    inputs = {key: value.long() for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        mel_spec = outputs.spectrogram.squeeze().cpu().numpy()

    # HiFi-GAN을 통해 음성으로 변환
    audio = mel_to_audio(mel_spec, hifi_gan)

    # 음성 파일 저장
    save_audio(audio, output_wav_path, sampling_rate)
    print(f"생성된 음성 파일이 {output_wav_path}로 저장되었습니다.")

if __name__ == "__main__":
    # 모델 로드
    model = VitsModel.from_pretrained("models/final_character_fine_tuned_model/").to('cuda')
    tokenizer = AutoTokenizer.from_pretrained("models/final_character_fine_tuned_model/")

    # HiFi-GAN vocoder 로드
    hifi_gan = load_hifi_gan_vocoder("hifi-gan/generator_v3")

    # 테스트 문장으로 TTS 실행
    test_text = "안녕하세요, 이것은 테스트 문장입니다."
    infer_tts(test_text, model, tokenizer, hifi_gan, output_wav_path="output.wav")
