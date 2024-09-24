## 디스코드 TTS 봇 "Raccoon"

![다운로드](https://github.com/user-attachments/assets/d0f28f10-28d5-4baf-8a12-88a458aaf1a5)

### 제작 목적
- 기존 TTS 봇들의 목소리가 마음에 들지 않아 바꿔달라는 요청에 제작하게 되었습니다.
- 특정 캐릭터들의 목소리를 지원해달라고 하여 제작 중입니다.
  - 현재 학습 중인 캐릭터 목소리
    - 트릭컬 리바이브 <코미>

### 제작 방법
- ```https://github.com/coqui-ai/TTS/releases/tag/v0.13.1``` 에서 zip 파일을 다운받거나 ```git clone https://github.com/coqui-ai/TTS.git``` 을 실행합니다.
  - Coqui TTS 를 클론받을 때 플젝 내부에서 최상단에 위치하게 한 뒤 다음과 같이 폴더를 생성합니다.
    
![화면 캡처 2024-09-19 185814](https://github.com/user-attachments/assets/928b3bb1-57f2-4da6-8b1c-38380f7a71e5)

- Coqui TTS 를 사용했고 ```metadata.csv``` 을 만들어 wav 파일과 문장, 발음을 저장했습니다.  
  - 발음 같은 경우 ```g2pk``` 라이브러리를 사용했고 위 ```metadata.py``` 파일에 적용되어 있습니다.
    
- ```scrap_voice.py``` 에서 스크랩할 유튜브 링크를 입력한 후 아래 ```start_time, end_time``` 부분에 시간초를 적어서 실행합니다.
  - ```output_segment``` 부분의 맨 끝에 segment 라고 적힌 것이 있는데 이 부분에 원하는 이름으로 바꾸면 됩니다.
    
- 위와 같이 설정했다면 학습 방법은 다음과 같습니다.
  - ```DiscordTTSBotRaccoon\TTS-0.13.1\TTS-0.13.1\recipes\ljspeech\vits_tts\train_vits.py``` 를 run 하면 학습이 시작됩니다.
  - ```VitsConfig``` 부분에서 ```epochs``` 수를 조절할 수 있으며, 검증 데이터 사이즈를 조절하는 ```eval_split_size``` 가 문제된다면 ```0.1 ~ 0.15``` 사이로 상황에 맞게 조절하시면 됩니다.
  - 이 이외의 에러가 발생시 필요한 라이브러리가 없거나 데이터 셋이 부족한 등의 이유가 대다수입니다.
