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
    {"wav_file": os.path.join(wav_directory, "segment_137.wav"), "text": "아무튼, 이런 날이 올 거라고 예상했어."},
    {"wav_file": os.path.join(wav_directory, "segment_138.wav"), "text": "비밀 모임 아고라 클럽에서 샤워 가운 입은 늙은이가 모든 지성체는 자신만의 이데아를 찾아야 하는 순간이 올 거라고 말했거든."},
    {"wav_file": os.path.join(wav_directory, "segment_139.wav"), "text": "통나무 속 헐벗은 늙은이는 그냥 다 때려치고 뒹굴거리며 살면 된다고 서로 싸우는게 거슬렸지만..."},
    {"wav_file": os.path.join(wav_directory, "segment_140.wav"), "text": "코미는 이미 알고 있었어! 둘 중 하나는 맞는 소리를 한다는 걸!"},
    {"wav_file": os.path.join(wav_directory, "segment_141.wav"), "text": "둘다 틀리고, 둘다 맞을 수 있지만... 어찌됐든 진정한 버터의 모습을 내가 도와주겠어!"},
    {"wav_file": os.path.join(wav_directory, "segment_142.wav"), "text": "아주... 철학적인 고찰이군. 좋은 자세야."},
    {"wav_file": os.path.join(wav_directory, "segment_143.wav"), "text": "그래 버터. 그러니까 멋도 모르고 물리학에 입문한 대학 새내기의 눈물 젖은 이과책은 갖다 버려!"},
    {"wav_file": os.path.join(wav_directory, "segment_144.wav"), "text": "날 따라와서 이 세상의 진리를 깨닫는 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_145.wav"), "text": "새 학생 데려왔어."},
    {"wav_file": os.path.join(wav_directory, "segment_146.wav"), "text": "쯧쯧.. 버터! 모든 일에는 순서가 있는 거야."},
    {"wav_file": os.path.join(wav_directory, "segment_147.wav"), "text": "기본 수강 코스부터 완료를 해야 심화 과정을 밟을 수 있는 거라고."},
    {"wav_file": os.path.join(wav_directory, "segment_148.wav"), "text": "그래서 에슈르는 새 학생 안 받을 거야?"},
    {"wav_file": os.path.join(wav_directory, "segment_149.wav"), "text": "거래한 대로 약속한 과자 한 봉지나 내놓으시지."},
    {"wav_file": os.path.join(wav_directory, "segment_150.wav"), "text": "모르면 배워야 해, 버터! 그게 목적이었잖아!"},
    {"wav_file": os.path.join(wav_directory, "segment_151.wav"), "text": "코미는 에슈르의 유토피아를 실현시켜주기 위해서 촉매 가속 작용을 돕고 있는 것 뿐이야!"},
    {"wav_file": os.path.join(wav_directory, "segment_152.wav"), "text": "코미는 기본 과정 옛날에 다 뗐으니깐 이만 가볼게."},
    {"wav_file": os.path.join(wav_directory, "segment_153.wav"), "text": "배움의 반복은 의미없는 짓이라고 주장할 거거든."},
    {"wav_file": os.path.join(wav_directory, "segment_154.wav"), "text": "그래. 그렇게 말해야지."},
    {"wav_file": os.path.join(wav_directory, "segment_155.wav"), "text": "에슈르, 다음엔 세 명을 한 번에 데려올테니까 그때도 잘 부탁해."},
    {"wav_file": os.path.join(wav_directory, "segment_156.wav"), "text": "코미가 신약 시험을 이틀 연속으로 받는 건 무리였나?"},
    {"wav_file": os.path.join(wav_directory, "segment_157.wav"), "text": "그래도 돈이 있으니까 치료약을 사먹으면 되겠지."},
    {"wav_file": os.path.join(wav_directory, "segment_158.wav"), "text": "엣? 뭐야? 에슈르랑 여왕님?"},
    {"wav_file": os.path.join(wav_directory, "segment_159.wav"), "text": "버터를 전자레인지에 돌렸어요? 빵집 주인이 그러면 어떻게 해?"},
    {"wav_file": os.path.join(wav_directory, "segment_160.wav"), "text": "그럼 말고요. 코미는 문과니까 이런 말해도 그냥 넘어갈 수 있어."},
    {"wav_file": os.path.join(wav_directory, "segment_161.wav"), "text": "이미 예상했던 일이군."},
    {"wav_file": os.path.join(wav_directory, "segment_162.wav"), "text": "비밀 모임 제자백가의 비단 가운을 입은 늙은이가 지성체는 태어날 때부터 사악하다고 했거든요."},
    {"wav_file": os.path.join(wav_directory, "segment_163.wav"), "text": "버터는... 자신만의 태생적 이데아를 찾은게 분명해요!"},
    {"wav_file": os.path.join(wav_directory, "segment_164.wav"), "text": "버터! 두 번째 섭종은 진짜 위험하다고!"},
    {"wav_file": os.path.join(wav_directory, "segment_165.wav"), "text": "코미는 버터를 팔아넘기지 않았어."},
    {"wav_file": os.path.join(wav_directory, "segment_166.wav"), "text": "그건 순수한 코미의 노동 보수였을 뿐이었어!"},
    {"wav_file": os.path.join(wav_directory, "segment_167.wav"), "text": "널 넘겨주는 대가로 정당하게 얻은 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_168.wav"), "text": "버터... 너는 물건이야?"},
    {"wav_file": os.path.join(wav_directory, "segment_169.wav"), "text": "코미는 너에 대한 가격을 매겨서 판매가로 널 에슈르에게 넘긴 적이 없다."},
    {"wav_file": os.path.join(wav_directory, "segment_170.wav"), "text": "코미는 그냥 중간에서 둘을 소개해주고 중계료를 받았을 뿐 널 사고 판 적이 없어!"},
    {"wav_file": os.path.join(wav_directory, "segment_171.wav"), "text": "경우가 다르지. 버터를 물건처럼 팔려면 과자 한 봉지로는 택도 없었을 거야."},
    {"wav_file": os.path.join(wav_directory, "segment_172.wav"), "text": "왜냐면 버터는... 과자 두 봉지 이상의 수인이니까."},
    {"wav_file": os.path.join(wav_directory, "segment_173.wav"), "text": "네~"},
    {"wav_file": os.path.join(wav_directory, "segment_174.wav"), "text": "코미가 알 바 아닌 듯. 코미는 알바비 받은 거로 오락실 갈거임."}
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


