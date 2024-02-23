import sys
sys.stdin = open("input.txt")

dr = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

for tc in range(int(input())):
    N, M, B = map(int, input().split())
    radio = [tuple(map(int, input().split())) for _ in range(B)]
    fly = [tuple(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            visited = [[0] * N for _ in range(N)]

            for x in range(i, i+M):
                for y in range(j, j+M):

                    if (x+1, y+1) in radio:
                        for di, dj in dr:
                            ni, nj = x + di, y + dj
                            if (0<=ni<N and 0<=nj<N) and not visited[ni][nj]:
                                kill += fly[ni][nj]
                                visited[ni][nj] = 1

                    if not visited[x][y]:
                        kill += fly[x][y]
                        visited[x][y] = 1

            max_kill = max(kill, max_kill)

    print(f'#{tc+1} {max_kill}')