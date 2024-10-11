import os
from g2pk import G2p

# G2P 객체 생성
g2p = G2p()

# 상대 경로로 저장할 디렉토리 경로 설정
base_dir = os.path.abspath("./DiscordTTSBotRaccoon/TTS-0.13.1/DataSet")
wav_directory = os.path.abspath(os.path.join(base_dir, "wavs"))
metadata_path = os.path.join(base_dir, "metadata.csv")

# 구간 설정 및 텍스트 정의
segments = [
    {"wav_file": os.path.join(wav_directory, "segment_xxx.wav"), "text": "입력하세요."}
    # 필요한 만큼 구간 추가 가능
]

# Coqui TTS 학습을 위한 metadata.csv 파일에 추가
with open(metadata_path, "a", encoding="utf-8") as metadata_file:
    for segment in segments:
        segment_wav = os.path.abspath(segment["wav_file"])
        
        # 파일 이름에서 확장자 제거
        segment_name = os.path.splitext(segment_wav)[0]
        
        text = segment["text"]
        phoneme_text = g2p(text)  # G2P 변환

        # metadata 파일에 '파일 이름|텍스트|음소 변환 텍스트' 형식으로 추가
        metadata_file.write(f"{segment_name}|{text}|{phoneme_text}\n")

print(f"Metadata 파일에 내용이 추가되었습니다: {metadata_path}")


