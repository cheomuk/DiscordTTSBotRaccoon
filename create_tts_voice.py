from TTS.api import TTS
import os

# 학습된 모델의 경로 설정 (best_model.pth와 config.json 파일이 있는 디렉토리)
model_path = ""
config_path = ""

# 경로가 실제로 존재하는지 확인
print("Model path exists:", os.path.exists(model_path))
print("Config path exists:", os.path.exists(config_path))

# TTS 모델 로드
tts = TTS(model_path=model_path, config_path=config_path)

# 생성할 텍스트 설정 (한국어 텍스트)
text = "안녕하세요, Coqui TTS를 사용하여 음성을 생성하고 있습니다."

# 음성 생성 및 저장
output_path = "output.wav"
tts.tts_to_file(text=text, file_path=output_path)

print(f"Generated speech saved at: {output_path}")
