import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = [list(int, input().split()) for _ in range(N)] # 1:N / 2:S

    for c in range(N):
        stack = []
        for r in range(N):
            m = arr[r][c]
            if m == 1:
                if stack:
                    
            elif m == 2:
