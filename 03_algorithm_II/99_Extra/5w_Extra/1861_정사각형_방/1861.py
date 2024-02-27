import sys
sys.stdin = open('input.txt')

dr = ((1, 0), (0, 1), (-1, 0), (0, -1))

for tc in range(int(input())):
    N = int(input())
    DP = [0] * (N**2+1)
    for r in range(N):
        for c, v in enumerate(map(int, input().split())):
            DP[v] = (r, c)

    min_v, max_l, cnt, v = 1, 1, 1, 1
    for n in range(1, len(DP)):
        i, j = DP[n]
        for di, dj in dr:
            if DP[n-1] == (i+di, j+dj):
                cnt += 1
                if max_l < cnt:
                    max_l, min_v = cnt, v
                break
        else:
            cnt, v = 1, n

    print(f'#{tc+1}', min_v, max_l)