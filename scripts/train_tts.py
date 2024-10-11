import os
import torch
from transformers import VitsModel, AutoTokenizer
from torch.utils.data import DataLoader
import logging
from preprocess import preprocess_wavs
from utils import collate_fn, waveform_to_mel, match_tensor_size
from TTSDataset import TTSDataset

# Configure logging
logging.basicConfig(level=logging.INFO)


def train_model(model, tokenizer, dataset_path, wav_dir, epochs=20, lr=1e-4, device='cuda'):
    # 데이터셋 준비
    dataset = TTSDataset(metadata_file=dataset_path, wav_dir=wav_dir)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=collate_fn)

    # 옵티마이저 설정
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    # 학습 루프
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch_idx, (texts, mels) in enumerate(dataloader):
            optimizer.zero_grad()

            # 텍스트 입력 처리
            inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True).to(device)
            mels = mels.to(device)

            # 모델 출력
            outputs = model(**inputs)
            predicted_waveform = outputs.waveform

            # 파형을 멜 스펙트로그램으로 변환
            predicted_waveform_np = predicted_waveform.squeeze(1).detach().cpu().numpy()
            predicted_mels = waveform_to_mel(predicted_waveform_np)

            # 멜 스펙트로그램 크기 맞추기
            predicted_mels, mels = match_tensor_size(predicted_mels, mels)
            predicted_mels = torch.tensor(predicted_mels, requires_grad=True).to(device)

            # 손실 계산 및 역전파
            loss = torch.nn.functional.mse_loss(predicted_mels, mels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

            # 배치별 로그 출력
            logging.info(f'Epoch [{epoch+1}/{epochs}], Batch [{batch_idx+1}/{len(dataloader)}], Loss: {loss.item():.4f}')
        
        # 에포크별 평균 손실 출력
        avg_loss = total_loss / len(dataloader)
        logging.info(f'Epoch [{epoch+1}/{epochs}] completed, Average Loss: {avg_loss:.4f}')

    return model



if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load pretrained model and tokenizer
    model = VitsModel.from_pretrained("facebook/mms-tts-kor").to(device)
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")

    # First stage: Fine-tuning on KSS dataset for pronunciation and intonation
    logging.info("Starting fine-tuning on KSS dataset...")
    model = train_model(model, tokenizer, '../data/metadata_kss.csv', '../data/kss', epochs=10, lr=1e-4, device=device)

    # Save intermediate model
    model.save_pretrained("../models/fine_tuned_model/")
    tokenizer.save_pretrained("../models/fine_tuned_model/")

    # Second stage: Fine-tuning on character dataset for tone
    logging.info("Starting fine-tuning on character dataset...")
    model = train_model(model, tokenizer, '../data/metadata_wavs.csv', '../data/wavs', epochs=10, lr=1e-5, device=device)

    # Save final model
    model.save_pretrained("../models/final_character_fine_tuned_model/")
    tokenizer.save_pretrained("../models/final_character_fine_tuned_model/")


