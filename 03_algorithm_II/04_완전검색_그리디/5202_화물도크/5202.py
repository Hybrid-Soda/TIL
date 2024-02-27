import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    W = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
    cnt, end = 1, W[0][1]
    for i in range(N-1):
        if end <= W[i+1][0]: end = W[i+1][1]; cnt += 1
    print(f'#{tc+1} {cnt}')