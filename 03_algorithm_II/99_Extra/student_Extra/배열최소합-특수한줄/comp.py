import sys
sys.stdin = open("input.txt")

# 백트래킹 + 순열
def make_per(start=0, idx=0, temp_sum=0):
    global min_sum
    if temp_sum >= min_sum:
        return
    if start == N-M:
        min_sum = min(min_sum, temp_sum)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            make_per(start+1, idx+1, temp_sum + arr[idx][i])
            visited[i] = 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    SL = tuple(map(int, input().split()))

    # 일반 줄과 특수 줄 분리
    arr = [list(map(int, input().split())) for _ in range(N)]
    spe_arr = [arr[i-1] for i in SL]
    for i in range(M):
        arr.pop(SL[i]-i-1)

    # 순열을 위한 배열
    visited = [0] * N
    min_sum = float('inf')

    # 일반 줄 최소합
    make_per()

    # 특수 줄 최소합
    for i in range(M):
        min_sum += min(spe_arr[i])

    print(f'#{tc+1}', min_sum)
