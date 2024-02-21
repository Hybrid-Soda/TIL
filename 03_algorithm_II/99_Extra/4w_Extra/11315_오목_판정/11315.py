import sys
sys.stdin = open('input.txt')

dr = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))

def search():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for di, dj in dr:
                    for k in range(1, 5):
                        ni, nj = i + k*di, j + k*dj
                        if not (0<=ni<N and 0<=nj<N) or board[ni][nj] != 'o':
                            break
                    else:
                        return 'YES'
    return 'NO'

for tc in range(int(input())):
    N = int(input())
    board = [input() for _ in range(N)]
    print(f'#{tc+1}', search())