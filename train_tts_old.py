import torch
from torch.utils.data import Dataset, DataLoader
from transformers import VitsModel, AutoTokenizer
import librosa
import numpy as np
import os
import logging  # logging 모듈 추가
from unidecode import unidecode
from waveform_to_mel import waveform_to_mel
from tensor_utils import match_tensor_size

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# unidecode를 사용하여 한글을 로마자로 변환하는 함수
def romanize_text(text):
    return unidecode(text)

# 커스텀 데이터셋 클래스
class TTSDataset(Dataset):
    def __init__(self, metadata_file, wav_dir):
        self.metadata = []
        with open(metadata_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                self.metadata.append((parts[0], parts[1]))  # 파일 이름과 텍스트
        self.wav_dir = wav_dir

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        wav_name, text = self.metadata[idx]
        wav_path = os.path.join(self.wav_dir, f"{wav_name}.wav")
        wav, sr = librosa.load(wav_path, sr=22050)
        mel_spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=80)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        # 텍스트를 로마자로 변환
        romanized_text = romanize_text(text)
        return romanized_text, mel_spec_db

# collate_fn 함수: 각 배치의 데이터를 패딩하여 크기를 맞추기
def collate_fn(batch):
    texts, mels = zip(*batch)

    # 텍스트는 그대로 두고, 멜 스펙트로그램의 최대 길이로 패딩
    max_mel_len = max([mel.shape[1] for mel in mels])
    
    # 패딩된 멜 스펙트로그램 배열을 만듦
    padded_mels = []
    for mel in mels:
        pad_len = max_mel_len - mel.shape[1]
        padded_mel = np.pad(mel, ((0, 0), (0, pad_len)), mode='constant')
        padded_mels.append(padded_mel)

    # 리스트 대신 numpy 배열로 변환 후 텐서로 변환
    padded_mels = np.array(padded_mels)
    return list(texts), torch.tensor(padded_mels)

# 파인튜닝 설정
def fine_tune_model(continue_training=True):   # 학습을 이어 할 것인지 새로할 것인지 설정
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 학습을 처음부터 시작할지 이어서 할지 결정
    if continue_training and os.path.exists("models/fine_tuned_model/pytorch_model.bin"):
        logging.info("이전 학습된 모델을 로드합니다.")
        model = VitsModel.from_pretrained("models/fine_tuned_model/")
        tokenizer = AutoTokenizer.from_pretrained("models/fine_tuned_model/")
    else:
        logging.info("새 모델을 로드합니다.")
        model = VitsModel.from_pretrained("facebook/mms-tts-kor")
        tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")

    model.to(device)

    # 데이터셋 및 DataLoader 준비
    dataset = TTSDataset("data/metadata_wavs.csv", "data/wavs/")
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=collate_fn)

    # Optimizer 설정
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

    # epoch 횟수 설정
    epochs = 1
    
    # 학습 후 PC 종료 여부
    turnoff_switch = True

    # 학습 루프
    model.train()
    logging.info("학습 시작")
    
    for epoch in range(epochs):
        total_loss = 0
        for batch_idx, (texts, mels) in enumerate(dataloader):
            optimizer.zero_grad()

            # 텍스트를 토큰화하고 LongTensor로 변환, max_length 추가
            inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
            inputs = {key: value.to(device).long() for key, value in inputs.items()}
            
            mels = mels.clone().detach().float().to(device)

            # 모델 출력에서 waveform을 사용
            outputs = model(**inputs)
            predicted_waveform = outputs.waveform

            # 예측된 파형을 멜 스펙트로그램으로 변환 (n_fft 값 조정)
            predicted_mels = waveform_to_mel(predicted_waveform.squeeze(1), n_mels=80, n_fft=1024)

            # 예측된 멜 스펙트로그램과 실제 멜 스펙트로그램의 크기를 맞추기
            predicted_mels, mels = match_tensor_size(predicted_mels, mels)

            # 손실 계산: 예측된 멜 스펙트로그램과 실제 멜 스펙트로그램 비교
            loss = torch.nn.functional.mse_loss(predicted_mels, mels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            
            # 배치별로 로그 출력
            logging.info(f'Epoch [{epoch+1}/{epochs}], Batch [{batch_idx+1}/{len(dataloader)}], Loss: {loss.item():.4f}')

        # 에포크별 평균 손실 로그 출력
        avg_loss = total_loss / len(dataloader)
        logging.info(f'Epoch [{epoch+1}/{epochs}] completed, Average Loss: {avg_loss:.4f}')

    # 파인튜닝된 모델 및 토크나이저 저장
    model.save_pretrained("models/fine_tuned_model/")
    tokenizer.save_pretrained("models/fine_tuned_model/")
    logging.info("모델과 토크나이저가 성공적으로 저장되었습니다.")
    
    # 학습 후 PC 종료
    if turnoff_switch:
        os.system("shutdown /s /f /t 0")

if __name__ == "__main__":
    fine_tune_model(continue_training=True)  # True로 설정하면 이전 모델 이어서 학습











