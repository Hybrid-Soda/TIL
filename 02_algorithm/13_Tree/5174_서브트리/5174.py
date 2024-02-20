import sys
sys.stdin = open('input.txt')

# 중위 순회
def inorder(now):
    if now:
        inorder(tree[now][0])
        global cnt; cnt += 1
        inorder(tree[now][1])

for tc in range(int(input())):
    E, N = map(int, input().split())  # E: 간선 개수 / N: 루트 노드
    edge = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(1002)]
    cnt = 0

    for i in range(len(edge)//2):
        if not tree[edge[2*i]][0]:
            tree[edge[2*i]][0] = edge[2*i+1]
        else:
            tree[edge[2*i]][1] = edge[2*i+1]

    inorder(N)
    print(f'#{tc+1}', cnt)