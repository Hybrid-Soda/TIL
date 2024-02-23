import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            kill = 0
            # 다이아몬드 모양으로 파리 퇴치
            for x in range(i-M//2, i+M//2+1):
                for y in range(j-M//2, j+M//2+1):
                    if (0<=x<N and 0<=y<N) and abs(x-i) + abs(y-j) <= M//2:
                        kill += fly[x][y]
            max_kill = max(max_kill, kill)

    print(f'#{tc+1}', max_kill)