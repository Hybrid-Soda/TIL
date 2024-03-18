import sys
sys.stdin = open('input.txt')

def quick_sort(start, end):
    stack = [(start, end)]

    while stack:
        start, end = stack.pop()

        if start < end:
            pivot_index = partition(start, end)
            stack.append((start, pivot_index - 1))
            stack.append((pivot_index + 1, end))

def partition(start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc+1}', arr[N//2])