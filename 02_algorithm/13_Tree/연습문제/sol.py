# 이진 트리 표현에 대하여 전위 순회하여 정점의 번호 출력

import sys
sys.stdin = open('input.txt')

# 노드번호 출력
def solution(k):
    print(k, end= ' ')

# 전위 순회
def preorder(now):
    if now:
        solution(now)
        preorder(tree[now][0])
        preorder(tree[now][1])

# 중위 순회
def inorder(now):
    if now:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

# 후위 순회
def postorder(now):
    if now:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)

V = int(input())
edge = list(map(int, input().split()))
E = len(edge)
tree = [[0, 0] for _ in range(V+1)]  # 이진 트리

for i in range(E//2):
    if not tree[edge[2*i]][0]:
        tree[edge[2*i]][0] = edge[2*i+1]
    else:
        tree[edge[2*i]][1] = edge[2*i+1]

preorder(1)
print()
inorder(1)
print()
postorder(1)
'''
                  1
            2           3
        4          5         6
    7           8     9   10    11
12                            13
'''