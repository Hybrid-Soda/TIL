# 4615 오셀로 게임
# 목표 : 게임이 끝난 후 흑돌, 백돌의 개수 출력

import sys
sys.stdin = open('input.txt')

dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

for tc in range(int(input())):
    # N: 보드 크기 / M: 착수 횟수
    N, M = map(int, input().split())

    # 보드 초기 세팅 (1: 흑돌 / 2: 백돌)
    board = [[0] * N for _ in range(N)]
    mid = N//2
    board[mid-1][mid-1: mid+1] = [2, 1]
    board[mid][mid-1: mid+1] = [1, 2]

    # 게임 진행
    for _ in range(M):
        i, j, team = map(int, input().split())
        i, j = i-1, j-1

        # 델타 탐색
        for di, dj in dir:
            ni, nj = i + di, j + dj
            sw = []

            # 단일 방향 심층 탐색
            while True:
                # 보드 범위 이탈 -> 종료
                if not (0<=ni<N and 0<=nj<N):
                    sw = []
                    break
                # 돌이 없는 칸 -> 종료
                if board[ni][nj] == 0:
                    sw = []
                    break
                # 같은 팀 돌 접촉 -> 뒤집기 예약 후 종료
                if board[ni][nj] == team:
                    break
                # 다른 팀 돌 접촉 -> 진행
                else:
                    sw.append((ni, nj))
                    ni += di; nj += dj
            
            # 조건을 만족한다면 뒤집기
            for si, sj in sw:
                if team == 1:
                    board[si][sj] = 1
                else:
                    board[si][sj] = 2

        board[i][j] = team

    # 점수 집계
    B, W = 0, 0
    for row in board:
        B += row.count(1)
        W += row.count(2)

    print(f'#{tc+1} {B} {W}')