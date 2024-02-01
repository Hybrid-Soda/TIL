def bubble_sort(arr, N):
    # 탐색 길이를 줄임 / 앞에서부터 줄임
    for i in range(N-1, 0, -1):
        for j in range(i):

            # 왼쪽수가 오른쪽수보다 크면 서로 자리 바꿈 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


def counting_sort(arr, N):
    K = max(arr)
    sort_arr = [0] * N

    # count 배열 생성
    count = [0] * (K+1)

    # count 배열 기록
    for i in arr:
        count[i] += 1

    # count 누적합 구하기
    for i in range(1, K+1):
        count[i] += count[i-1]

    # arr의 마지막 원소부터 정렬 (N-1 -> 0)
    for i in range(N-1, -1, -1):
        # 개수를 인덱스로 변환
        idx = count[arr[i]]
        idx -= 1
        sort_arr[idx] = arr[i]

    return sort_arr


def selection_sort(arr, N):
    # 배열 순회
    for i in range(N-1):
        min_idx = i

        # 최소값 찾기 / 초기 최소값 이후 인덱스부터
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 서로 자리 바꿈
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    
    return arr   
