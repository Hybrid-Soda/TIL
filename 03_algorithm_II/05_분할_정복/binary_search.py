# while문 사용
def binary_search(arr, key):
    # 최소, 최대 인덱스 초기화
    low, high = 0, len(arr) - 1

    # 양 끝 인덱스가 겹칠 때까지
    while low <= high:
        mid = (low + high) // 2

        # 값 비교 - 값을 찾았다면 인덱스 반환
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    # 찾는 값이 없으면 -1 반환
    return -1


# 재귀함수 사용
def binary_search(arr, low, high, key):
    # 찾는 값이 없으면 -1 반환
    if low > high:
        return -1
    
    # mid 값 초기화
    mid = (low + high) // 2
    
    # 값을 찾았다면 인덱스 반환
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, low, mid-1, key)
    else:
        return binary_search(arr, mid+1, high, key)