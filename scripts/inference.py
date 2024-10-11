import torch
from transformers import VitsModel, AutoTokenizer
import soundfile as sf
from utils import normalize_waveform

def load_model(model_dir):
    model = VitsModel.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    return model, tokenizer

def tts_inference(text, model, tokenizer, output_wav_path="output.wav", sampling_rate=22050):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to('cuda')
    with torch.no_grad():
        outputs = model(**inputs)
        waveform = outputs.waveform.squeeze().cpu().numpy()

    # Normalize waveform and save as a WAV file
    waveform = normalize_waveform(waveform)
    sf.write(output_wav_path, waveform, sampling_rate)

if __name__ == "__main__":
    model, tokenizer = load_model("models/final_character_fine_tuned_model/")
    test_text = "이건 테스트 문장입니다."
    tts_inference(test_text, model, tokenizer)
