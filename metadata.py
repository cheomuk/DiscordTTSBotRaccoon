import os
from g2pk import G2p

# G2P 객체 생성
g2p = G2p()

# 상대 경로로 저장할 디렉토리 경로 설정
wav_directory = "./"
metadata_path = os.path.join(wav_directory, "metadata.csv")

# 구간 설정 및 텍스트 정의
segments = [
    {"wav_file": os.path.join(wav_directory, "segment_1.wav"), "text": "으음? 뭐야, 버터 여기서 뭐해?"},
    {"wav_file": os.path.join(wav_directory, "segment_2.wav"), "text": "코미는 여기 근처에서 알바해."},
    {"wav_file": os.path.join(wav_directory, "segment_3.wav"), "text": "무슨 약 같은거 먹으면 돈 줘. 코미는 그 돈으로 간식 먹고 게임하고 놀아."},
    {"wav_file": os.path.join(wav_directory, "segment_4.wav"), "text": "코미가 먼저 물었잖아. 대답 안 할거야?"},
    {"wav_file": os.path.join(wav_directory, "segment_5.wav"), "text": "어어.. 양성자 물리학과 핵융합 이론? 이게 무슨 책인데?"},
    {"wav_file": os.path.join(wav_directory, "segment_6.wav"), "text": "으으.. 코미는 무슨 말인지 모르겠다. 공부는 왜 하는데?"},
    {"wav_file": os.path.join(wav_directory, "segment_7.wav"), "text": "버터 또 바보 취급 당했구나?"},
    {"wav_file": os.path.join(wav_directory, "segment_8.wav"), "text": "버터 없는 자리에서 모두 버터 바보라고 얘기하는 모임이 있어."},
    {"wav_file": os.path.join(wav_directory, "segment_9.wav"), "text": "엄밀히 말하면 코미의 머릿 속에서만 이루어지는 비밀 모임이니까 어디 가서 말하지는 말아줘."}
    # 필요한 만큼 구간 추가 가능
]

# Coqui TTS 학습을 위한 metadata.csv 파일에 추가
with open(metadata_path, "a", encoding="utf-8") as metadata_file:
    for segment in segments:
        segment_wav = segment["wav_file"]
        text = segment["text"]
        phoneme_text = g2p(text)  # G2P 변환

        # metadata 파일에 'WAV 파일 경로|텍스트|음소 변환 텍스트' 형식으로 추가
        metadata_file.write(f"{segment_wav}|{text}|{phoneme_text}\n")

print(f"Metadata 파일에 내용이 추가되었습니다: {metadata_path}")


