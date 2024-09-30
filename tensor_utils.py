import torch

# 텐서 크기를 맞추기 위한 함수
def match_tensor_size(tensor1, tensor2):
    """
    두 텐서의 크기를 맞추기 위해서 잘라내거나 패딩합니다.
    Args:
        tensor1 (Tensor): 첫 번째 텐서 (predicted_mels)
        tensor2 (Tensor): 두 번째 텐서 (mels)
    Returns:
        Tensor, Tensor: 크기가 동일하게 맞춰진 두 텐서
    """
    # 두 텐서의 길이를 비교하여 작은 길이에 맞추기
    min_length = min(tensor1.shape[-1], tensor2.shape[-1])
    tensor1 = tensor1[:, :, :min_length]
    tensor2 = tensor2[:, :, :min_length]
    
    return tensor1, tensor2
