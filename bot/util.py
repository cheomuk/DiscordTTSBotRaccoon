import os
import librosa
import numpy as np

def __getitem__(self, idx):
    wav_name, text = self.metadata[idx]
    wav_path = os.path.join(self.wav_dir, f"{wav_name}.wav")
    wav, sr = librosa.load(wav_path, sr=22050)  # 오디오 파일 로드
    mel_spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=80)  # y와 sr을 명시적으로 전달
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)  # 데시벨로 변환
    return text, mel_spec_db

