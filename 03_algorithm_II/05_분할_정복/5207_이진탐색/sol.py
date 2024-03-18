import sys
sys.stdin = open('input.txt')

def binary_search(arr, key):
    low, high = 0, N - 1
    temp = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            if temp == 1: return 0
            low = mid + 1
            temp = 1
        else:
            if temp == 2: return 0
            high = mid - 1
            temp = 2

    return 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for num in B:
        if binary_search(A, num): ans += 1

    print(f'#{tc+1}', ans)