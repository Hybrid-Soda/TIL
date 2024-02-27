import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N, cnt = int(input()), 0
    arr = [x for _ in range(N) for x in input().split()]
    s = ''

    for c in range(N):
        for r in range(0, N*N, N):
            if arr[r+c] != '0': s += arr[r+c]
            else: continue
        cnt += s.count('12')
        s = ''

    print(f'#{tc+1} {cnt}')