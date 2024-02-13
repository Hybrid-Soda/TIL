# 4875 미로

import sys
sys.stdin = open('input.txt')

# 델타탐색 - 상우좌하 순서
direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for tc in range(int(input())):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    ans = 0

    # 시작 좌표 찾기
    for num in range(N):
        if '2' in maze[num]:
            i, j = num, maze[num].index('2')
    stack = [(i, j)]

    # 미로 찾기 - DFS / stack이 빌 때까지 반복
    while stack:
        # 현재 좌표 설정 및 표시
        i, j = stack.pop()
        maze[i][j] = '1'

        # 주변 탐색
        for di, dj in direction:
            ni = i + di; nj = j + dj
            if 0<=ni<N and 0<=nj<N:
                if maze[ni][nj] == '3':
                    ans = 1
                    break
                if maze[ni][nj] == '0':
                    stack.append((ni, nj))
        # 탐색을 마쳤는데도 3이 없으면 다음 루프 시작
        else:
            continue

    print(f'#{tc+1} {ans}')