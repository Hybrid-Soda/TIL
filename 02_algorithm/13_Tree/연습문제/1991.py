def preorder(now):
    if now:
        print(sw[now], end='')
        preorder(tree[now][0])
        preorder(tree[now][1])

def inorder(now):
    if now:
        inorder(tree[now][0])
        print(sw[now], end='')
        inorder(tree[now][1])

def postorder(now):
    if now:
        postorder(tree[now][0])
        postorder(tree[now][1])
        print(sw[now], end='')

sw = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
tree = [[0, 0] for _ in range(N+1)]

for _ in range(N):
    p, c1, c2 = map(lambda x: sw.index(x), input().split())
    tree[p][0] = c1
    tree[p][1] = c2

preorder(1); print(); inorder(1); print(); postorder(1)