import torch

print(torch.cuda.is_available())  # True일 경우 CUDA 사용 가능
print(torch.version.cuda)  # 설치된 PyTorch의 CUDA 버전 출력

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# CUDA 가 인식 안 된 채 진행되고 있었어서 CUDA, Cudnn, PyTorch, Toolkit 버전을 맞추는 중입니다.
# 위 코드는 연결에 성공했는지 테스트하는 코드입니다.
# 현재 시도한 버전들, 실패 사례입니다. (GPU : RTX 2070 Super)
# ==============================================================================
# 1. CUDA : 최신 버전, Cudnn : 최신 버전, torch : 12.5, toolkit : 최신 버전 -> 실패
# 2. CUDA : 10.2, Cudnn : 8.6.0, torch : 1.12.1, toolkit : 10.2 -> 실패
# 3. CUDA : 11.8, Cudnn : 8.9.0 ~ 8.9.7, torch : 2.4.0, toolkit : 11.8 -> 실패
# 4. CUDA : 11.2, Cudnn : 8.1.0, torch : 1.10.1, toolkit : 11.2 -> 시도 중