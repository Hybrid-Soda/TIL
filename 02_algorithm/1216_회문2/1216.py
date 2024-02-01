# 1216 회문2
# 글자의 길이가 고정되어 있지 않음
# 가장 긴 회문의 길이를 구하라

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    test_case = int(input())
    board = [list(input()) for _ in range(100)]
    turn_board = [list(tuple) for tuple in zip(*board)]
    max_length = 0
    
    for N in range(1, 25):
        # 가로
        for row in board:
            for col in range(101-N):
                rvs = row[col:col+N]
                rvs.reverse()
                if row[col:col+N] == rvs:
                    max_length = len(rvs)
        
        # 세로
        for row in turn_board:
            for col in range(101-N):
                rvs = row[col:col+N]
                rvs.reverse()
                if row[col:col+N] == rvs:
                    max_length = len(rvs)

    print(f'#{test_case} {max_length}')