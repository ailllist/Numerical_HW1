import numpy as np

arr1d: np.ndarray = np.random.rand(5000) * 100

if len(arr1d.shape) >= 2:
    print("정렬 불가")
    exit()

if isinstance(arr1d[0], np.int32) or isinstance(arr1d[0], np.int64) or isinstance(arr1d[0], np.float64):
    pass
else:
    print("정렬 불가")
    exit()

for i in range(len(arr1d)):
    minimum_index = i
    for j in range(i + 1, len(arr1d)):
        if arr1d[j] < arr1d[minimum_index]:
            minimum_index = j
    arr1d[i], arr1d[minimum_index] = arr1d[minimum_index], arr1d[i]
