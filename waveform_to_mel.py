# waveform_to_mel.py

import torchaudio

# 파형을 멜 스펙트로그램으로 변환하는 함수
def waveform_to_mel(waveform, sr=22050, n_mels=80, n_fft=1024):
    """
    파형 데이터를 멜 스펙트로그램으로 변환합니다.
    Args:
        waveform (Tensor): 파형 데이터 (waveform)
        sr (int): 샘플링 레이트 (default 22050)
        n_mels (int): 멜 스펙트로그램의 멜 밴드 수 (default 80)
        n_fft (int): FFT 윈도우 크기 (default 1024)
    Returns:
        Tensor: 멜 스펙트로그램 (dB 변환된 값)
    """
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=sr, n_mels=n_mels, n_fft=n_fft)
    mel_spec = transform(waveform)
    mel_spec_db = torchaudio.transforms.AmplitudeToDB()(mel_spec)
    return mel_spec_db

