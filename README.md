## 디스코드 TTS 봇 "Raccoon"

![다운로드](https://github.com/user-attachments/assets/d0f28f10-28d5-4baf-8a12-88a458aaf1a5)

### 제작 목적
- 기존 TTS 봇들의 목소리가 마음에 들지 않아 바꿔달라는 요청에 제작하게 되었습니다.
- 특정 캐릭터들의 목소리를 지원해달라고 하여 제작 중입니다.
  - 현재 학습 중인 캐릭터 목소리
    - 트릭컬 리바이브 <코미>

### 제작 시도
- facebook 의 mms-tts-kor 을 불러와 KSS 음성 데이터를 epochs 20회 정도 학습시킨 뒤 캐릭터 목소리를 fined tuning 하도록 설계했습니다.
- epochs 10회 결과 모델은 생성됐지만 기계음 밖에 나지 않아 학습 옵션을 튜닝 중에 있습니다.
- vocoder 로 hifi_gan 모델을 선정했으며 학습 옵션 튜닝이 끝난 후 테스트해 볼 예정입니다.
  
