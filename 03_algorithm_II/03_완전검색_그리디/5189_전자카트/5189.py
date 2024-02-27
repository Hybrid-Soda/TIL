import sys
sys.stdin = open("input.txt")

def permu(i):
    if i == N - 1:
        global min_v
        cnt = 0
        path = [1] + num + [1]
        for j in range(len(path) - 1):
            cnt += arr[path[j] - 1][path[j + 1] - 1]
        min_v = min(min_v, cnt)
        return
    for j in range(i, N - 1):
        num[i], num[j] = num[j], num[i]
        permu(i + 1)
        num[i], num[j] = num[j], num[i]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(2, N + 1)]
    min_v = 100 * N
    permu(0)

    print(f"#{tc+1} {min_v}")
