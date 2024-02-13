# 1226 미로1

import sys
sys.stdin = open('input.txt')

# 델타탐색 - 좌하상우 순서
direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for tc in range(10):
    T = int(input())
    maze = [list(input()) for _ in range(16)]
    i, j = 1, 1; stack = [(i, j)]
    ans = 0
    # 미로 찾기 - DFS / stack이 빌 때까지 반복
    while stack:
        # 현재 좌표 설정 및 표시
        i, j = stack.pop()
        maze[i][j] = '1'

        # 주변 탐색
        for di, dj in direction:
            ni = i + di; nj = j + dj
            if maze[ni][nj] == '3':
                ans = 1
                break
            if maze[ni][nj] == '0':
                stack.append((ni, nj))
        # 탐색을 마쳤는데도 3이 없으면 다음 루프 시작
        else:
            continue

    print(f'#{T} {ans}')
