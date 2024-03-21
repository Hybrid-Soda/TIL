import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

ds = ((0,1), (1,0), (0,-1), (-1,0))
INF = float('inf')

for tc in range(int(input())):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    Q = []; heappush(Q, (0, 0, 0))
    dist = [[INF] * N for _ in range(N)]; dist[0][0] = 0

    while Q:
        w, i, j = heappop(Q)

        # 가지치기
        if dist[i][j] < w: continue

        # 델타탐색
        for di, dj in ds:
            ni, nj = i + di, j + dj

            # 범위
            if 0 <= ni < N and 0 <= nj < N:
                new_cost = w + max(0, graph[ni][nj] - graph[i][j]) + 1

                # 비용비교
                if dist[ni][nj] > new_cost:
                    dist[ni][nj] = new_cost
                    heappush(Q, (new_cost, ni, nj))

    print(f'#{tc+1} {dist[-1][-1]}')