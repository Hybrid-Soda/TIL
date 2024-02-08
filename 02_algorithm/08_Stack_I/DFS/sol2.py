# stack을 활용한 DFS (인접 행렬 사용 방식)

import sys
sys.stdin = open('input.txt')


def DFS(start):
    stack = [start]
    
    while stack:
        now = stack.pop()  # LIFO
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')
        # for next in range(1, V+1):
        for next in range(V, 0, -1):
            if visited[next] == 0 and adj[now][next] == 1:
                stack.append(next)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V+1)

# 인접 행렬
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    adj[arr[i*2]][arr[i*2+1]] = 1
    adj[arr[i*2+1]][arr[i*2]] = 1

DFS(1)