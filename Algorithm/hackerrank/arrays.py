import numpy as np 

arr = [1, 2, 3, 4, -8, -10]
res = np.array(arr, float)
print(res)
a = np.sort(res)[::-1]
print(a)