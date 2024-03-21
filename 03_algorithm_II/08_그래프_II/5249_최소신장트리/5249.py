import sys
sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx < ry: parent[ry] = rx
    else: parent[rx] = ry

for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    parent, ans = list(range(V+1)), 0

    for s, e, w in graph:        # 오름차순 정렬된 그래프를 순회
        if find(s) != find(e):   # 같은 트리에 속하는지 확인 (순환 그래프 회피)
            union(s, e)          # 같지 않으면 병합
            ans += w

    print(f'#{tc+1}', ans)