import sys
sys.stdin = open('input.txt')

def merge(left_hand, right_hand):
    result = []
    l, r = 0, 0

    while l < len(left_hand) and r < len(right_hand):
        if left_hand[l] < right_hand[r]:
            result.append(left_hand[l]); l += 1
        else:
            result.append(right_hand[r]); r += 1

    result += left_hand[l:]
    result += right_hand[r:]

    if left_hand[-1] > right_hand[-1]:
        global cnt; cnt += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_hand = arr[:mid]
    right_hand = arr[mid:]

    left_hand = merge_sort(left_hand)
    right_hand = merge_sort(right_hand)

    return merge(left_hand, right_hand)


for tc in range(int(input())):
    N = int(input()); cnt = 0
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)
    print(f'#{tc+1}', arr[N//2], cnt)