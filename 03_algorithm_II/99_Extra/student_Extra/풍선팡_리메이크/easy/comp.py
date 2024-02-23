import sys
sys.stdin = open("input.txt")

odd = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
even = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pang(i, j, is_odd):
    temp = arr[i][j]
    for di, dj in is_odd:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            temp += arr[ni][nj]
    return temp

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] % 2 == 0:
                max_v = max(max_v, pang(i, j, even))
            else:
                max_v = max(max_v, pang(i, j, odd))

    print(f'#{tc+1}', max_v)
