import numpy as np  # numpy 배열을 사용


def selection_sort(arr1d: np.ndarray) -> np.ndarray:  # 함수 선언
    if len(arr1d.shape) >= 2:  # 이차원 배열 이상인 경우
        print("정렬 불가")  # 정렬 불가 출력후
        exit()  # 코드 종료
    
    if isinstance(arr1d[0], np.int32) or isinstance(arr1d[0], np.int64) or isinstance(arr1d[0], np.float64):
        pass  # arr1d[0]이 int나 float인 경우는 넘기고
    else:  # 그 외인 경우는
        print("정렬 불가")  # 정렬 불가 출력후
        exit()  # 코드 종료
    
    for i in range(len(arr1d)):  # arr1d순회, index 0부터 시작
        minimum_index = i  # 최소 값인 index를 찾는다.
        for j in range(i + 1, len(arr1d)):  # 최소 값 이후 부터 탐색 진행
            if arr1d[j] < arr1d[minimum_index]:  # 최소 값보다 더 작은 값을 찾으면
                minimum_index = j  # 최소값 index 갱신
        arr1d[i], arr1d[minimum_index] = arr1d[minimum_index], arr1d[i]  # 가장 작은 값과 i번째 요소를 바꿈
    
    return arr1d


arr_1 = np.random.rand(5000) * 100  # 5000개의 무작위 배열 생성
selection_sort(arr_1)  # 함수 진행
