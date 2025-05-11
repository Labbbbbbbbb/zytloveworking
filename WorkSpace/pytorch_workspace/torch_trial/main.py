import torch
print(torch.__version__)
print(torch.cuda.is_available())

tensor_a = torch.arange(0,12)
print(tensor_a)

print(torch.cuda.is_available())
print(torch.backends.cudnn.is_available())
print(torch.cuda_version)
print(torch.backends.cudnn.version())
print(1)

