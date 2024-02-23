import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = 0
            # 파리채 크기
            for x in range(i, i+M):
                for y in range(j, j+M):
                    kill += fly[x][y]
            # 구멍 크기
            for x in range(i+1, i+M-1):
                for y in range(j+1, j+M-1):
                    kill -= fly[x][y]
            max_kill = max(max_kill, kill)
    
    print(f'#{tc+1} {max_kill}')
