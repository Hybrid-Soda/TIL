import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

for tc in range(int(input())):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [int(1e9)] * (N+1); dist[0] = 0

    # 그래프 제작
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
    
    # 다익스트라
    Q = []; heappush(Q, (0, 0))
    while Q:
        w, now = heappop(Q)

        if dist[now] < w: continue

        for cost, next in graph[now]:
            new_cost = w + cost
            if dist[next] > new_cost:
                dist[next] = new_cost
                heappush(Q, (new_cost, next))

    print(f'#{tc+1} {dist[N]}')