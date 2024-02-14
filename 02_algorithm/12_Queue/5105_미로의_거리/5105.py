# 5105 미로의 거리

import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for tc in range(int(input())):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    ans = 0

    # 시작 좌표 찾기
    for num in range(N):
        if '2' in maze[num]:
            i, j = num, maze[num].index('2')
    
    # BFS 미로 찾기
    Q = deque([(i, j, 0)])
    while Q:
        i, j, dist = Q.popleft()

        # 델타 탐색
        for di, dj in dr:
            ni = i + di; nj = j + dj
            if 0<=ni<N and 0<=nj<N:
                # 3을 찾으면 종료
                if maze[ni][nj] == '3':
                    break
                # 통로를 찾으면 queue에 좌표와 거리를 추가
                if maze[ni][nj] == '0':
                    Q.append((ni, nj, dist+1))
        # 델타 탐색에서 3을 찾지 못했다면 현재 점 표시 후 다음으로 이동
        else:
            maze[i][j] = '1'
            continue
        # 3을 찾았으므로 답은 최소 거리
        ans = dist
        break
    
    print(f'#{tc+1} {ans}')