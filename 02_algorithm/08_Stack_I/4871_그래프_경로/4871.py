# 4871 그래프 경로

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())         # 노드 개수, 간선 개수
    routes = [[] for _ in range(V+1)]        # 루트 배열
    for _ in range(E):                       # 루트 입력 예시 [[], [4, 3], [3, 5], [6], []]
        s, e = map(int, input().split())     # 인덱스가 시작점 / 값이 도착점
        routes[s].append(e)
    start, end = map(int, input().split())   # 시작점, 도착점
    visit = [0] * (V+1)                      # 방문 장소 체크
    stack = [start]                          # 스택 시작점 할당
    is_exist = 0                             # 답

    # DFS : 스택에 원소가 없거나 도착점에 도달하면 종료
    while stack:
        now = stack[-1]
        if now == end:
            is_exist = 1
            break

        # 현재점과 연결된 도착점 파악
        for next in routes[now]:
            # 도착점이 방문한 곳이 아니라면 현재점에 방문표시하고 도착점 방문
            if not visit[next]:
                visit[now] = 1
                stack.append(next)
                break
        # 도착점이 없거나 도착점에 모두 방문했다면 이전점에서 탐색
        else:
            visit[now] = 1
            stack.pop()

    print(f'#{tc+1} {is_exist}')
