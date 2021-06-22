import numpy as np
a=np.zeros((3,2))
b=np.ones([3,3])
c=np.eye(3)
d=np.random.randn(2,3)
print(a)
print(b)
print(c)
print(b+c)
print(d)
print(np.full([2, 3], 42))
# Range with start, end and step
print(np.arange(10, 90, 3))
# Equally spaced numbers in a range
print(np.linspace(3, 27, 9))#the last paramater indicates the number of elements we need in the range