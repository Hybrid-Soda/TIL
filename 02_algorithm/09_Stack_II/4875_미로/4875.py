# 4875 미로
# 1. 델타탐색 실행
# 2. 0이 있는 부분 stack에 추가
# 3. 

import sys
sys.stdin = open('input.txt')
from pprint import pprint

#     상  우 좌  하
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]


def mazerunner(maze):
    try:
        i, j = [N-1, maze[-1].index('2')]
        stack = [[i, j]]

        while stack:
            pprint(maze)
            print(f'stack : {stack}')
            print(f'pos : {i,j}')
            # 델타 탐색
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if maze[ni][nj] == '0':
                        stack.append([ni, nj])
                        i, j = ni, nj
                        break
                    if maze[ni][nj] == '3':
                        return 1
            else:
                i, j = stack.pop()
            maze[i][j] = '1'
        if not stack:
            return 0
    except:
        return 0


for tc in range(int(input())):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    print(f'#{tc+1} {mazerunner(maze)}')