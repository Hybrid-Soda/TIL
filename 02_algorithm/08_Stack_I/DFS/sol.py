# stack을 활용한 DFS (인접 리스트 사용 방식)

import sys
sys.stdin = open('input.txt')


def DFS(start):
    stack = [start]
    
    while stack:
        now = stack.pop()  # LIFO
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')
        for next in adj[now]:
            if visited[next] == 0:
                stack.append(next)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj = [[] for _ in range(V + 1)]

# 무 방향 그래프 : 반대로도 입력
for i in range(0, E*2, 2):
    adj[arr[i]].append(arr[i+1])
    adj[arr[i+1]].append(arr[i])

visited = [0] * (V+1)

DFS(1)