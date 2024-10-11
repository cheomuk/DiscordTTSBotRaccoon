import torch
from torch.utils.data import Dataset
import librosa
import os
import numpy as np
from unidecode import unidecode

class TTSDataset(Dataset):
    def __init__(self, metadata_file, wav_dir):
        self.metadata = []
        with open(metadata_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                self.metadata.append((parts[0], parts[1]))  # filename and text
        self.wav_dir = wav_dir

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        wav_name, text = self.metadata[idx]
        wav_path = os.path.join(self.wav_dir, f"{wav_name}.wav")
        wav, sr = librosa.load(wav_path, sr=22050)
        mel_spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=80)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        # Romanize the text for the tokenizer (if required)
        romanized_text = unidecode(text)
        return romanized_text, torch.tensor(mel_spec_db)
