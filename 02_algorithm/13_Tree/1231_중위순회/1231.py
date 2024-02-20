import sys
sys.stdin = open('input.txt')

# 중위 순회
def inorder(now):
    if now:
        inorder(tree[now][1])
        print(tree[now][0], end='')
        inorder(tree[now][2])

for tc in range(10):
    N = int(input().strip())
    tree = [[0, 0, 0] for _ in range(N+1)]

    for _ in range(N):
        p, *etc = input().split()  # p: 1 / etc: ['W', '2', '3']
        tree[int(p)][0] = etc[0]   # 문자 저장

        try:
            tree[int(p)][1] = int(etc[1])  # 왼쪽 자식 저장
            tree[int(p)][2] = int(etc[2])  # 오른쪽 자식 저장
        except:
            pass

    print(f'#{tc+1} ', end='')
    inorder(1)
    print()