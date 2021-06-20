import numpy as np 
kanto=np.array([73,67,43])
w1=0.2
w2=0.3
w3=0.5
weights=np.array([w1,w2,w3])
print(np.dot(kanto,weights))
print((kanto*weights).sum())
new_array=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(new_array.shape)
print(new_array.dtype)