import librosa
import os
import numpy as np

def preprocess_wavs(wav_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for wav_file in os.listdir(wav_dir):
        if wav_file.endswith('.wav'):
            wav_path = os.path.join(wav_dir, wav_file)
            wav, sr = librosa.load(wav_path, sr=22050)
            mel_spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=80)
            mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

            np.save(os.path.join(output_dir, wav_file.replace('.wav', '.npy')), mel_spec_db)

if __name__ == "__main__":
    preprocess_wavs('data/kss', 'data/kss_mels')
    preprocess_wavs('data/wavs', 'data/wavs_mels')
