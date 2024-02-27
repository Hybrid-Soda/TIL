import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    DP = arr[0]

    for r in range(N):
        for c in range(N):
            if c and r: DP[c] = min(DP[c], DP[c-1]) + arr[r][c]
            elif c and not r: DP[c] += DP[c-1]
            elif not c and r: DP[c] += arr[r][c]

    print(f'#{tc+1} {DP[-1]}')


# 완전탐색
'''
dx = [0, 1]
dy = [1, 0]

def stack(x, y):
    stack = [(0, 0, data[0][0])]
    while stack:
        x, y, cnt = stack.pop()
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N:
                if visited[nx][ny] > cnt + data[nx][ny]:
                    visited[nx][ny] = cnt + data[nx][ny]
                    stack.append((nx, ny, cnt + data[nx][ny]))

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[N*N*10] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            stack(j, i)

    print(f'#{tc+1} {visited[N-1][N-1]}')
'''