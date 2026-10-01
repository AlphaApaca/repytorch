import torch
import numpy as np
#
# Initializing a tensor
#
data = [[1,2], [3,4]]
x_data = torch.tensor(data)
print(f"Tensor from data: \n {x_data} \n")

np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"Tensor from NumPy array: \n {x_np} \n")

x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")
x_rand = torch.rand_like(x_data, dtype=torch.float32)
print(f"Random Tensor: \n {x_rand} \n")

shape = (2,3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")
#
# Attributes of a Tensor
#
tensor = torch.rand(3,4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
print(f"Tensor: \n {tensor} \n")
#
# Operations on Tensors
#
if torch.mps.is_available():
    tensor = tensor.to("mps") # PyTorch 会在内部把字符串转换成 torch.device 对象
print(f"Device tensor is stored on: {tensor.device}")

tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:,0]}")
print(f"Last column: {tensor[...,-1]}")
tensor[:,1] = 0
print(tensor)

# Joining tensors
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)
print(f"t1 shape: {t1.shape}")

# Arithmetic operations
# This computes the matrix multiplication between two tensors. 
# y1, y2, y3 will have the same value
# "tensor.T" returns the transpose of the tensor.
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)
y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out=y3)

# This computes the element-wise product.
# z1, z2, z3 will have the same value
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
# print(f"y1: \n {y1} \n")
# print(f"z1: \n {z1} \n")
# print(f"y3: \n {y3} \n")
# print(f"z3: \n {z3} \n")
# Aggregating tensors
agg = tensor.sum()
agg_item = agg.item()
print(f"agg: {agg}, agg_item: {agg_item}, type(agg): {type(agg)}, type(agg_item): {type(agg_item)}")
# In-place operations
print(f"{tensor} \n")
tensor.add_(5)
print(tensor)
#
# Bridge with NumPy
#
# Tensors to NumPy array
t = torch.ones(5)
print(f"t: {t} \n")
n = t.numpy()
print(f"n: {n} \n")
print(t.device)

t.add_(1)
print(f"t: {t}")
print(f"n: {n}")
# NumPy array to Tensor
n = np.ones(5)
t = torch.from_numpy(n)

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")

x = torch.tensor(2.0, requires_grad=True)
y = x * x
y.backward()
print(x.grad)  # dy/dx = 2x = 4.0
