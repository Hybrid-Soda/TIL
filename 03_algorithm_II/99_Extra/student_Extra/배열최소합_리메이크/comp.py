import sys
sys.stdin = open("input.txt")

# 백트래킹 + 순열
def make_per(start=0, idx=0, temp_sum=0):
    global min_sum
    if temp_sum >= min_sum:
        return
    if start == N:
        min_sum = min(min_sum, temp_sum)
        return
    for i in range(N):
        if visited[i] < 2:
            visited[i] += 1
            make_per(start+1, idx+1, temp_sum + arr[idx][i])
            visited[i] -= 1

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = float('inf')

    make_per()

    print(f'#{tc+1}', min_sum)
    