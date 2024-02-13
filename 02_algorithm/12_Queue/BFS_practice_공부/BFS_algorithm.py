from collections import deque

def DFS(G, v): # G : 그래프 / v : 탐색 시작점
    visited = [0] * (n+1)
    Q = deque()
    Q.append(v)

    # Q가 비어있지 않은 경우
    while Q:
        elmt = Q.popleft()

        # 방문하지 않았던 곳이라면 방문 표시하고 할일함
        if not visited[elmt]:
            visited[elmt] = True
            visit(elmt)            # 정점에서 할 일

            # elmt와 연결된 모든 정점에 대해 방문하지 않았다면 큐에 삽입
            for i in G[elmt]:
                if not visited[i]:
                    Q.append(i)