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
    
    # 찾는 문자열의 길이
    for N in range(1, 25):
        # 가로 방향으로 회문 찾기
        for row in range(100):
            for col in range(101-N):
                if row[col:col+N] == row[col+N-1:col-1:-1]:
                    max_length = N
                if row[col:col+N] == row[col+N-1:col-1:-1]:
                    max_length = N
        
        # 세로 방향으로 회문 찾기
        for row in turn_board:
            for col in range(101-N):
                if row[col:col+N] == row[col+N-1:col-1:-1]:
                    max_length = N

    print(f'#{test_case} {max_length}')