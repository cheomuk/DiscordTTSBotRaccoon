import torch
import numpy as np
import soundfile as sf
from hifi_gan.models import Generator

# HiFi-GAN vocoder 불러오기
def load_hifi_gan_vocoder(model_path):
    hifi_gan = Generator(80)  # 80은 Mel-spectrogram의 필터 개수
    checkpoint = torch.load(model_path, map_location='cpu')
    hifi_gan.load_state_dict(checkpoint['generator'])
    hifi_gan.eval()
    hifi_gan.remove_weight_norm()
    return hifi_gan

# Mel-spectrogram을 음성으로 변환하는 함수
def mel_to_audio(mel_spec, hifi_gan):
    with torch.no_grad():
        mel_tensor = torch.FloatTensor(mel_spec).unsqueeze(0)  # Batch size 추가
        audio = hifi_gan(mel_tensor).squeeze().cpu().numpy()
    return audio

# 음성 파일로 저장하는 함수
def save_audio(audio, file_name, sampling_rate=22050):
    sf.write(file_name, audio, sampling_rate)
