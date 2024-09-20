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
    {"wav_file": os.path.join(wav_directory, "segment_48.wav"), "text": "너 요정들한테 잡혔다가 도망친거야?"},
    {"wav_file": os.path.join(wav_directory, "segment_49.wav"), "text": "자, 여기 이것 좀 먹고 힘내."},
    {"wav_file": os.path.join(wav_directory, "segment_50.wav"), "text": "어때, 괜찮지? 미끼로 쓰는 물건인데 맛은 좋아... 헤헤..."},
    {"wav_file": os.path.join(wav_directory, "segment_51.wav"), "text": "응. 이걸 이용해서 요정들이 우릴 잡아간대. 너도 잡힌거 아니었어?"},
    {"wav_file": os.path.join(wav_directory, "segment_52.wav"), "text": "코... 코미."},
    {"wav_file": os.path.join(wav_directory, "segment_53.wav"), "text": "나도 몰라... 그냥 그렇게 들었어..."},
    {"wav_file": os.path.join(wav_directory, "segment_54.wav"), "text": "사... 사료스탕스."},
    {"wav_file": os.path.join(wav_directory, "segment_55.wav"), "text": "사!료!스!탕!스!"},
    {"wav_file": os.path.join(wav_directory, "segment_56.wav"), "text": "수인들을 사악한 요정의 압제로부터 자유롭게 하려는 우리 부락의 민족 해방 전선 단체야."},
    {"wav_file": os.path.join(wav_directory, "segment_57.wav"), "text": "우, 우리도 처음 보는 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_58.wav"), "text": "음, 그러니까 한 달 전에 처음 봤었어...!"},
    {"wav_file": os.path.join(wav_directory, "segment_59.wav"), "text": "한 달 전에 마을에 상자가 무진장 배달됐어!"},
    {"wav_file": os.path.join(wav_directory, "segment_60.wav"), "text": "그리고 그 다음 주에도 수백 상자가 왔어!"},
    {"wav_file": os.path.join(wav_directory, "segment_61.wav"), "text": "그 다음 주에도 또 왔고! 신속 정확 정기 배송이래!"},
    {"wav_file": os.path.join(wav_directory, "segment_62.wav"), "text": "응, 맞아! 정기 택배래!"},
    {"wav_file": os.path.join(wav_directory, "segment_63.wav"), "text": "보내는 자가 요정 여왕 에르핀이라고 쓰여 있었어."},
    {"wav_file": os.path.join(wav_directory, "segment_64.wav"), "text": "저기..."},
    {"wav_file": os.path.join(wav_directory, "segment_65.wav"), "text": "이 길 따라서 쭉 가. 코미는 그냥 여기 있을게."},
    {"wav_file": os.path.join(wav_directory, "segment_66.wav"), "text": "아무래도 안 되겠어. 코미가 요정들이랑 어울리는 걸 보면 분명 해코지당할 거야."},
    {"wav_file": os.path.join(wav_directory, "segment_67.wav"), "text": "수인들은 동족 의식이 강해서 사소한 꼬투리로도 사회적 마찰을 일으키니까."},
    {"wav_file": os.path.join(wav_directory, "segment_68.wav"), "text": "한 번 품은 이념은 편견 같은 거라서 쉽게 사그라들지 않는 거래."},
    {"wav_file": os.path.join(wav_directory, "segment_69.wav"), "text": "코미가 주운 빨간색 책에서 읽었어."},
    {"wav_file": os.path.join(wav_directory, "segment_70.wav"), "text": "코미는 이미 사료 먹는거 들켜서 눈 밖에 나있어. 그냥 어디에 숨어있을래."},
    {"wav_file": os.path.join(wav_directory, "segment_71.wav"), "text": "그치만... 코미 무서워..."},
    {"wav_file": os.path.join(wav_directory, "segment_72.wav"), "text": "또 잡혀가면 잠도 안 재우고 수련 같은거 시킨단 말이야."},
    {"wav_file": os.path.join(wav_directory, "segment_73.wav"), "text": "사료스탕..."},
    {"wav_file": os.path.join(wav_directory, "segment_74.wav"), "text": "히에엑...."},
    {"wav_file": os.path.join(wav_directory, "segment_75.wav"), "text": "베, 베니?!"},
    {"wav_file": os.path.join(wav_directory, "segment_76.wav"), "text": "저기... 코미가 말하면 안 돼? 베니는 내 친구야."},
    {"wav_file": os.path.join(wav_directory, "segment_77.wav"), "text": "웅! 베니! 나는 잡혀있는 거 아니야!"},
    {"wav_file": os.path.join(wav_directory, "segment_78.wav"), "text": "요정들은 오해를 풀고 싶어서 왔대! 사료 같은거 요정들이 꾸민 짓이 아니래!"},
    {"wav_file": os.path.join(wav_directory, "segment_79.wav"), "text": "이 맛 좋은 사료에는 아무런 음모도 없는 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_80.wav"), "text": "그러니까 그냥 맘 편히 먹어도 된다는 뜻이야!"},
    {"wav_file": os.path.join(wav_directory, "segment_81.wav"), "text": "코미는 사료가 좋단 말이야! 매일 열매 따먹는 거나 사냥하는 거 귀찮아!"},
    {"wav_file": os.path.join(wav_directory, "segment_82.wav"), "text": "사료는 뚜껑만 따서 그냥 바로 먹을 수 있잖아! 베니도 한 입만 해보라니까!"},
    {"wav_file": os.path.join(wav_directory, "segment_83.wav"), "text": "우아앙! 코미가 걱정하던 대로 됐어! 코미는 이제 몰라! 숨을 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_84.wav"), "text": "사천왕...? 하지만 사료스탕스는..."},
    {"wav_file": os.path.join(wav_directory, "segment_85.wav"), "text": "너희... 쎄구나?"},
    {"wav_file": os.path.join(wav_directory, "segment_86.wav"), "text": "베니는 사료스탕스에서 제일 힘 쎈데... 너희가 이겼어...!"},
    {"wav_file": os.path.join(wav_directory, "segment_87.wav"), "text": "힘은 센데 힘을 잘 쓸 줄 모르는 친구이긴 해."},
    {"wav_file": os.path.join(wav_directory, "segment_88.wav"), "text": "아무튼 너희는 이제 코미와 친구야! 코미도 이제부터 같이 싸울게!"},
    {"wav_file": os.path.join(wav_directory, "segment_89.wav"), "text": "코미가 앞장서서 길 안내할 테니까 따라와!"},
    {"wav_file": os.path.join(wav_directory, "segment_90.wav"), "text": "음... 우우움...."},
    {"wav_file": os.path.join(wav_directory, "segment_91.wav"), "text": "그게... 그러니까..."},
    {"wav_file": os.path.join(wav_directory, "segment_92.wav"), "text": "코미는 길 모르겠어."},
    {"wav_file": os.path.join(wav_directory, "segment_93.wav"), "text": "코미는 길을 기억하는게 아니야. 익숙한 냄새를 따라가는 거야."},
    {"wav_file": os.path.join(wav_directory, "segment_94.wav"), "text": "근데... 냄새가 여기저기서 나..."},
    {"wav_file": os.path.join(wav_directory, "segment_95.wav"), "text": "사료 냄새."},
    {"wav_file": os.path.join(wav_directory, "segment_96.wav"), "text": "그건 코미보다 멍청한 말이야."},
    {"wav_file": os.path.join(wav_directory, "segment_97.wav"), "text": "사료가 많이 많이 배달된 걸 마을에 쌓아놓고 있어서 그 냄새를 따라간 거였는데..."},
    {"wav_file": os.path.join(wav_directory, "segment_98.wav"), "text": "이상해. 지금 여기서는 사방에서 사료 깡통 냄새가 마구마구 나서 어디로 가야 할지 모르겠어."},
    {"wav_file": os.path.join(wav_directory, "segment_99.wav"), "text": "나, 나도 한 입만!"},
    {"wav_file": os.path.join(wav_directory, "segment_100.wav"), "text": "쟤는 내 마을 친구 버터야."},
    {"wav_file": os.path.join(wav_directory, "segment_101.wav"), "text": "웅웅! 오랜만이다, 버터!"},
    {"wav_file": os.path.join(wav_directory, "segment_102.wav"), "text": "코미 그런 거 몰라. 이제 얘네가 내 친구야."},
    {"wav_file": os.path.join(wav_directory, "segment_103.wav"), "text": "얘네가 이기면 사료 마음대로 먹을 수 있어."},
    {"wav_file": os.path.join(wav_directory, "segment_104.wav"), "text": "사료스탕스를 물리치면 사료를 눈치 안 보고 먹을 수 있어!"},
    {"wav_file": os.path.join(wav_directory, "segment_105.wav"), "text": "그래! 버터도 숨겨놓고 몰래 먹는 거 그만해도 돼!"},
    {"wav_file": os.path.join(wav_directory, "segment_106.wav"), "text": "무슨 말인진 잘 모르겠지만 다 될 거야! 코미의 육차 산업 혁명의 꿈도 이룰 수 있어!"},
    {"wav_file": os.path.join(wav_directory, "segment_107.wav"), "text": "코미 몰라. 그냥 주운 책에서 읽었어. 멋있는 단어잖아."},
    {"wav_file": os.path.join(wav_directory, "segment_108.wav"), "text": "코미 패거리 출동이야! 헤헤!"},
    {"wav_file": os.path.join(wav_directory, "segment_109.wav"), "text": "이게 정상이야."},
    {"wav_file": os.path.join(wav_directory, "segment_110.wav"), "text": "병사가 뭐야?"},
    {"wav_file": os.path.join(wav_directory, "segment_111.wav"), "text": "사료스탕스는..."},
    {"wav_file": os.path.join(wav_directory, "segment_112.wav"), "text": "하지만... 엄청 쎄!"},
    {"wav_file": os.path.join(wav_directory, "segment_113.wav"), "text": "사료스탕스... 엄청 쎄!"},
    {"wav_file": os.path.join(wav_directory, "segment_114.wav"), "text": "한 명의 강함은 곧... 부족 전체의 강함이나 다름없지."},
    {"wav_file": os.path.join(wav_directory, "segment_115.wav"), "text": "사료스탕스 조심해야 해!"},
    {"wav_file": os.path.join(wav_directory, "segment_116.wav"), "text": "숨어 들어가야 해! 사료스탕스한테 걸리면 힘들어질 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_117.wav"), "text": "코, 코미가 막을게...! 베니 멈춰!"},
    {"wav_file": os.path.join(wav_directory, "segment_118.wav"), "text": "코미는 세뇌 같은 거 안 당했어!"},
    {"wav_file": os.path.join(wav_directory, "segment_119.wav"), "text": "코미는 그냥 편하게 살고 싶을 뿐이야! 베니도 사실 그렇잖아?"},
    {"wav_file": os.path.join(wav_directory, "segment_120.wav"), "text": "매일 꿀통 털다가 벌한테 쏘이는 거 지겹지도 않아?"},
    {"wav_file": os.path.join(wav_directory, "segment_121.wav"), "text": "사료만 있으면 그런 일 안 해도 배부르게 살 수 있다구!"},
    {"wav_file": os.path.join(wav_directory, "segment_122.wav"), "text": "코미는 애완동물 아니야! 이런 건 상호보완적인 관계라고 하는 거라고!"},
    {"wav_file": os.path.join(wav_directory, "segment_123.wav"), "text": "코미는 세뇌당한 거 아니라고!"},
    {"wav_file": os.path.join(wav_directory, "segment_124.wav"), "text": "베니가 귀를 틀어막았어!"},
    {"wav_file": os.path.join(wav_directory, "segment_125.wav"), "text": "으으응... 그냥 너희가 다 먹겠다는 뜻이잖아! 코미도 사료 먹을 거야!"},
    {"wav_file": os.path.join(wav_directory, "segment_126.wav"), "text": "코미와 함께 사료를 독점하려는 생계형 범죄급 악의 축을 물리치자!"},
    {"wav_file": os.path.join(wav_directory, "segment_127.wav"), "text": "으윽! 티, 티그다! 사료스탕스의 대장 티그야!"},
    {"wav_file": os.path.join(wav_directory, "segment_128.wav"), "text": "노예? 코미는... 으으음..."},
    {"wav_file": os.path.join(wav_directory, "segment_129.wav"), "text": "노예 제도는 구시대에서 빈번히 발생한 사회 기반 시스템이니까,"},
    {"wav_file": os.path.join(wav_directory, "segment_130.wav"), "text": "아직 국가 체계를 수립하지 못한 수인 부락에서는 나름 효율적이지 않을까?"},
    {"wav_file": os.path.join(wav_directory, "segment_131.wav"), "text": "그치만 코미는 주운 책에서 그렇게 읽었는 걸?"},
    {"wav_file": os.path.join(wav_directory, "segment_132.wav"), "text": "코미가 말했잖아! 사료스탕스 엄청 쎄다구!"},
    {"wav_file": os.path.join(wav_directory, "segment_133.wav"), "text": "촌장 늙어서 약해!"},
    {"wav_file": os.path.join(wav_directory, "segment_134.wav"), "text": "우아아아아앙!!! 코미도 먹고 싶었는데!"},
    {"wav_file": os.path.join(wav_directory, "segment_135.wav"), "text": "사료... 다 내 꺼였는데..."},
    {"wav_file": os.path.join(wav_directory, "segment_136.wav"), "text": "코미는 모든게 허망해..."}
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


