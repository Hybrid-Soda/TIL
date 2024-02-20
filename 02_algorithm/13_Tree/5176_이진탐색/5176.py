# 5176 이진탐색

import sys
sys.stdin = open('input.txt')

# 값 저장
def write(now):
    global num
    tree[now][0] = num
    num += 1

# 중위 순회
def inorder(now):
    if 0 < now <= N:
        inorder(tree[now][1])
        write(now)
        inorder(tree[now][2])

for tc in range(int(input())):
    N = int(input()); num = 1
    tree = [[0, 2*i, 2*i+1] for i in range(N+1)]
    inorder(1)
    print(f'#{tc+1} {tree[1][0]} {tree[N//2][0]}')