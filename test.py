from TTS.api import TTS

# Load your trained TTS model
tts = TTS(model_path=".", config_path="config.json", vocoder_path="..\\vocoder")

# Synthesize speech
tts.tts_to_file(text="안녕하세요, 테스트 중입니다.", file_path="output.wav")
