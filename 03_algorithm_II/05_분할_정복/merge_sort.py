# 분할 함수
def merge_sort(arr):
    # 단일 원소까지 분할
    if len(arr) <= 1:
        return arr

    # 왼쪽과 오른쪽 배열로 분할
    mid = len(arr) // 2
    left_hand = arr[:mid]
    right_hand = arr[mid:]

    # 분할 함수 재귀
    merge_sort(left_hand)
    merge_sort(right_hand)

    # 왼쪽과 오른쪽 배열을 합병
    return merge(left_hand, right_hand)

# 정복 및 합병 함수
def merge(left_hand, right_hand):
    # 반환 배열과 왼쪽과 오른쪽에 대한 인덱스 초기화
    result = []
    l, r = 0, 0

    # 왼쪽이나 오른쪽 중 인덱스 초과까지 반복
    while l < len(left_hand) and r < len(right_hand):
        # 왼쪽 원소의 크기가 오른쪽보다 작으면 왼쪽 원소 배열에 추가
        if left_hand[l] < right_hand[r]:
            result.append(left_hand[l])
            l += 1
        # 왼쪽 원소의 크기가 오른쪽보다 크면 오른쪽 원소 배열에 추가
        else:
            result.append(right_hand[r])
            r += 1

    # 남은 부분 배열 모두 추가
    result += left_hand[l:]
    result += right_hand[r:]

    return result