import torch
import librosa
import numpy as np

def waveform_to_mel(waveform, n_mels=80, n_fft=1024):
    mel_spec = librosa.feature.melspectrogram(y=waveform, sr=22050, n_mels=n_mels, n_fft=n_fft)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    return torch.tensor(mel_spec_db)

def match_tensor_size(tensor1, tensor2):
    min_len = min(tensor1.size(-1), tensor2.size(-1))
    return tensor1[..., :min_len], tensor2[..., :min_len]

def normalize_waveform(waveform):
    return waveform / max(abs(waveform))

def collate_fn(batch):
    texts, mels = zip(*batch)

    # Pad mel-spectrograms to the longest in the batch
    max_mel_len = max([mel.shape[1] for mel in mels])
    padded_mels = []
    for mel in mels:
        pad_len = max_mel_len - mel.shape[1]
        padded_mel = np.pad(mel, ((0, 0), (0, pad_len)), mode='constant')
        padded_mels.append(padded_mel)

    # Convert the padded mel-spectrograms to tensors
    padded_mels = torch.tensor(padded_mels)
    
    return list(texts), padded_mels