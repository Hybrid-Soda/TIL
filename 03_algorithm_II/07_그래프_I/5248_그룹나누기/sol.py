import sys
sys.stdin = open('input.txt')

# 방법1 - DFS 사용
def DFS(now):
    visited[now] = 1
    for next in graph[now]:
        if not visited[next]:
            DFS(next)

for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited, cnt = [0] * (N+1), 0

    # 그래프 제작
    for i in range(0, 2*M, 2):
        graph[nums[i]].append(nums[i+1])
        graph[nums[i+1]].append(nums[i])

    # 숫자 순회 하며 방문하지 않았으면 DFS
    for i in range(1, N+1):
        if not visited[i]:
            DFS(i); cnt += 1

    print(f'#{tc+1}', cnt)

# 방법2 - 유니온 사용
def root(x, prnt):
    if prnt[x] != x:
        prnt[x] = root(prnt[x], prnt)
    return prnt[x]

def union(x, y, prnt):
    rx, ry = root(x, prnt), root(y, prnt)
    if rx == ry:
        return
    if rx <= ry:
        prnt[ry] = rx
    else:
        prnt[rx] = ry

for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    prnt = [i for i in range(N+1)]

    for i in range(0, 2*M, 2):
        union(nums[i], nums[i+1], prnt)

    print(f'#{tc+1}', len(set(root(i, prnt) for i in range(1, N+1))))
