import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # N: 노드 개수 / M: 리프 노드 개수 / L: 지정 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)

    # 트리에 리프 노드 값 저장
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    
    # 자식 노드 값의 합을 부모 노드에 저장
    for i in range(N-M, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]

    print(f'#{tc+1}', tree[L])
