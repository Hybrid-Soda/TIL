import sys
sys.stdin = open("input.txt")

def per(i, sum_v):
    global min_v
    if sum_v >= min_v: return
    if i == N: min_v = min(min_v, sum_v); return
    for j in range(i, N):
        num[i], num[j] = num[j], num[i]
        per(i+1, sum_v + cost[i][num[i]])
        num[i], num[j] = num[j], num[i]

for tc in range(int(input())):
    N, min_v = int(input()), 1500
    cost = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(N)]
    per(0, 0)
    print(f'#{tc+1} {min_v}')