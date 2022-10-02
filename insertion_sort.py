import numpy as np  # numpy 배열을 사용


def insertion_sort(arr1d: np.ndarray) -> np.ndarray:  # 함수 선언
    if len(arr1d.shape) >= 2:  # 이차원 배열 이상인 경우
        print("정렬 불가")  # 정렬 불가 출력후
        exit()  # 코드 종료
    
    if isinstance(arr1d[0], np.int32) or isinstance(arr1d[0], np.int64) or isinstance(arr1d[0], np.float64):
        pass  # arr1d[0]이 int나 float인 경우는 넘기고
    else:  # 그 외인 경우는
        print("정렬 불가")  # 정렬 불가 출력후
        exit()  # 코드 종료
    
    for i in range(1, len(arr1d)):  # arr1d 순회, index 0부터 시작
        cur = arr1d[i]  # 지금 숫자 저장
        j = i - 1  # 지금의 index보다 작은 부분을 탐색
        while j >= 0 and arr1d[j] > cur:  # 앞부분의 배열이 cur보다 큰 경우에만
            arr1d[j + 1] = arr1d[j]  # 오른쪽으로 한칸씩 민다
            j = j - 1  # j 감소
        arr1d[j + 1] = cur  # cur보다 작은 위치에 cur을 집어넣는다.
    
    return arr1d

arr_1 = np.random.rand(5000) * 100 # 5000개의 무작위 배열 생성
insertion_sort(arr_1) # 함수 진행
