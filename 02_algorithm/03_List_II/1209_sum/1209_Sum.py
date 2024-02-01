# 1209 Sum

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    turn_arr = list(zip(*arr))  # 세로 계산을 위한 회전 행렬

    # 최대값 초기화
    row_max, col_max = 0, 0
    cross1, cross2 = 0, 0

    # 각 행의 합을 구해 최대값 갱신
    for row in arr:
        row_max = max(row_max, sum(row))

    # 각 열의 합을 구해 최대값 갱신
    for col in turn_arr:
        col_max = max(col_max, sum(col))

    # 각 대각선의 합을 구함
    for i in range(100):
        cross1 += arr[i][i]
        cross2 += arr[i][99-i]
    
    # 각 합들 중 최대값 출력
    print(f'#{test_case} {max(row_max, col_max, cross1, cross2)}')



