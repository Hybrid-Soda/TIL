import sys
sys.stdin = open('input.txt')

def task(i, per):
    global ans
    if per <= ans: return
    if i == N: ans = max(ans, per); return
    for j in range(i, N):
        nums[i], nums[j] = nums[j], nums[i]
        task(i+1, per*(P[i][nums[i]]/100))
        nums[i], nums[j] = nums[j], nums[i]

for tc in range(int(input())):
    N, ans = int(input()), 0
    P = [list(map(int, input().split())) for _ in range(N)]
    nums = [i for i in range(N)]
    task(0, 1)
    print(f'#{tc+1} {ans*100:.6f}')