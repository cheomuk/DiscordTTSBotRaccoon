import os
from g2pk import G2p

# G2P 객체 생성
g2p = G2p()

# 상대 경로로 저장할 디렉토리 경로 설정
base_dir = os.path.abspath("./DiscordTTSBotRaccoon/TTS-0.13.1/DataSet")
wav_directory = os.path.join(base_dir, "wavs")
metadata_path = os.path.join(base_dir, "metadata.csv")

# 구간 설정 및 텍스트 정의
segments = [
    {"wav_file": os.path.join(wav_directory, "segment_45.wav"), "text": "핫!? 요, 요정?!"},
    {"wav_file": os.path.join(wav_directory, "segment_46.wav"), "text": "으아앙! 그만 따라와!!"},
    {"wav_file": os.path.join(wav_directory, "segment_47.wav"), "text": "뭐...? 넌 요정이 아니잖아?"},
    {"wav_file": os.path.join(wav_directory, "segment_48.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_49.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_50.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_51.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_52.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_53.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_54.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_55.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_56.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_57.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_58.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_59.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_60.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_61.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_62.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_63.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_64.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_65.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_66.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_67.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_68.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_69.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_70.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_71.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_72.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_73.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_74.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_75.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_76.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_77.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_78.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_79.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_80.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_81.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_82.wav"), "text": ""},
    {"wav_file": os.path.join(wav_directory, "segment_83.wav"), "text": ""}
    # 필요한 만큼 구간 추가 가능
]

# Coqui TTS 학습을 위한 metadata.csv 파일에 추가
with open(metadata_path, "a", encoding="utf-8") as metadata_file:
    for segment in segments:
        segment_wav = segment["wav_file"]
        
        # 파일 이름에서 확장자 제거
        segment_name = os.path.splitext(os.path.basename(segment_wav))[0]
        
        text = segment["text"]
        phoneme_text = g2p(text)  # G2P 변환

        # metadata 파일에 '파일 이름|텍스트|음소 변환 텍스트' 형식으로 추가
        metadata_file.write(f"{segment_name}|{text}|{phoneme_text}\n")

print(f"Metadata 파일에 내용이 추가되었습니다: {metadata_path}")


