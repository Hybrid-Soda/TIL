# 1974 스도쿠 검증

import sys
sys.stdin = open("input.txt")

def check_arr(arr, ans):
    for i in range(9):
        if len(set(arr[i])) != 9:
            ans = 0
            break
    return ans

for tc in range(int(input())):
    ans = 1
    arr_1 = [list(map(int, input().split())) for _ in range(9)]
    arr_2 = list(zip(*arr_1))
    arr_3 = [[] for _ in range(9)]

    # 3x3 격자
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            arr_3[i + j//3].extend(arr_1[i][j:j+3])
            arr_3[i + j//3].extend(arr_1[i+1][j:j+3])
            arr_3[i + j//3].extend(arr_1[i+2][j:j+3])
    
    # 가로 줄 확인
    ans = check_arr(arr_1, ans)

    # 세로 줄 확인
    if ans == 1:
        ans = check_arr(arr_2, ans)

    # 3x3 격자 확인
    if ans == 1:
        ans = check_arr(arr_3, ans)

    print(f'#{tc+1} {ans}')