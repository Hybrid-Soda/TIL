# 1215 회문1

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    turn_board = [list(tuple) for tuple in zip(*board)]
    ans = 0
    
    # 가로 방향으로 회문 찾기
    for row in board:
        for col in range(9-N):
            rvs = row[col:col+N]
            rvs.reverse()
            if row[col:col+N] == rvs:
                ans += 1
    
    # 세로 방향으로 회문 찾기
    for row in turn_board:
        for col in range(9-N):
            rvs = row[col:col+N]
            rvs.reverse()
            if row[col:col+N] == rvs:
                ans += 1

    print(f'#{tc+1} {ans}')