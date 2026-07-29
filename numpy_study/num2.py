import numpy as np
array_1d = np.array([10, 20, 30, 40, 50])
print(array_1d[1])
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array_2d[0,1])
array_oo = np.array([1, 2, 3, 4, 5, 6])
array_ooo = array_oo.reshape(2, 3)
print(array_ooo)