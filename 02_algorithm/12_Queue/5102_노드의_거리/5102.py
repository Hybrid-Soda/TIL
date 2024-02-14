# 5102 노드의 거리
# 목표 : 출발 노드에서 도착 노드까지의 최소 거리 구하기

import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # V: 노드 개수 / E: 간선 개수
    V, E = map(int, input().split())
    # 경로 정보
    routes = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        routes[start].append(end)
        routes[end].append(start)
    # S: 출발 노드 / G: 도착 노드
    S, G = map(int, input().split())
    # 각 노드별 출발점으로부터 거리
    distance = [0] * (V+1)
    
    # BFS - Q에 원소가 없으면 종료
    # 원소가 없어서 종료되었다는 뜻은 도착 노드까지 연결되어 있지 않다는 뜻
    Q = deque([S])
    while Q:
        now = Q.popleft()
        # G에 도달하면 종료
        if now == G:
            break
        # G에 도달하지 못했으면 다음 노드 탐색
        for next in routes[now]:
            # 다음 노드가 방문하지 않은 곳이라면 queue에 추가 후 거리 표시
            if not distance[next]:
                Q.append(next)
                distance[next] = distance[now] + 1

    print(f'#{tc+1} {distance[G]}')

