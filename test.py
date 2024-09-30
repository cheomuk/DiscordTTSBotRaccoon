import torch
from transformers import VitsModel, AutoTokenizer
import soundfile as sf
from unidecode import unidecode

# 텍스트를 로마자화하는 함수 (unidecode 사용)
def romanize_text(text):
    return unidecode(text)

# 저장된 모델과 토크나이저를 불러옵니다
def load_model_and_tokenizer(model_dir="models/fine_tuned_model/"):
    model = VitsModel.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)  # 토크나이저도 같은 디렉토리에서 불러오기
    model.eval()  # 평가 모드로 전환
    return model, tokenizer

# 파형을 정규화하는 함수
def normalize_waveform(waveform):
    max_val = max(abs(waveform))
    if max_val > 0:
        waveform = waveform / max_val  # 파형을 [-1, 1] 범위로 정규화
    return waveform

def tts_inference(text, model, tokenizer, output_wav_path="output.wav", sampling_rate=22050):
    # 입력 텍스트를 로마자화
    romanized_text = romanize_text(text)
    
    # 로마자화된 텍스트를 토큰화
    inputs = tokenizer(romanized_text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # 입력 토큰이 제대로 생성되었는지 확인
    if inputs['input_ids'].shape[1] == 0:
        raise ValueError(f"토크나이저가 '{romanized_text}' 텍스트를 처리할 수 없습니다. 입력 텍스트를 확인하세요.")

    # 입력을 LongTensor로 변환
    inputs = {key: value.long() for key, value in inputs.items()}

    # 모델을 사용하여 음성 파형을 예측
    with torch.no_grad():
        outputs = model(**inputs)

    # 모델 출력 확인
    if hasattr(outputs, 'waveform') and outputs.waveform is not None:
        waveform = outputs.waveform.squeeze().cpu().numpy()
        print(f"생성된 음성 파형의 길이: {len(waveform)}")
        print(f"생성된 파형 데이터 샘플: {waveform[:10]}")  # 처음 몇 개의 데이터를 확인

        # 파형을 정규화
        waveform = normalize_waveform(waveform)
        
        if len(waveform) > 0:
            # 다양한 샘플링 레이트를 시도하여 음성 파일로 저장
            sf.write(output_wav_path, waveform, sampling_rate)
            print(f"생성된 음성 파일이 {output_wav_path}로 저장되었습니다. (샘플링 레이트: {sampling_rate}Hz)")
        else:
            print("음성 파형 생성 실패: 생성된 음성 파형이 비어 있습니다.")
    else:
        print("모델 출력에 음성 파형이 없습니다.")

# 테스트 실행
if __name__ == "__main__":
    model_dir = "models/fine_tuned_model/"
    model, tokenizer = load_model_and_tokenizer(model_dir)

    # 긴 문장으로 테스트
    test_text = "이건 테스트 코드일 뿐이야. 이건 테스트 코드일 뿐이야. 이건 테스트 코드일 뿐이야."
    tts_inference(test_text, model, tokenizer)