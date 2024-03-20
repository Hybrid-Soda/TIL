import sys
sys.stdin = open("input.txt")

from collections import deque

for tc in range(10):
    L, S = map(int, input().split())
    link = list(map(int, input().split()))
    graph = [set() for _ in range(101)]
    dist = [0] * 101; dist[S] = 1
    ans = 0

    # 그래프 제작
    for i in range(0, L, 2):
        graph[link[i]].add(link[i+1])

    # BFS
    Q = deque([S])
    while Q:
        now = Q.popleft()
        for next in graph[now]:
            if not dist[next]:
                dist[next] = dist[now] + 1
                Q.append(next)
    
    print(f'#{tc+1}', 100 - dist[::-1].index(max(dist)))