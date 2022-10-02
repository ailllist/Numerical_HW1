import numpy as np


def insertion_sort(arr1d: np.ndarray) -> np.ndarray:
    if len(arr1d.shape) >= 2:
        print("정렬 불가")
        exit()
    
    if isinstance(arr1d[0], np.int32) or isinstance(arr1d[0], np.float64):
        pass
    else:
        print("정렬 불가")
        exit()
        
    for i in range(1, len(arr1d)):
        cur = arr1d[i]
        j = i - 1
        while j >= 0 and arr1d[j] > cur:
            arr1d[j + 1] = arr1d[j]
            j = j-1
        arr1d[j+1] = cur
        
    return arr1d


arr_1 = np.array([4, 5, 1, 2, 8, 15, 32, 12, 3])
# arr_1 = np.array([4.4, 5.1])
print(insertion_sort(arr_1))