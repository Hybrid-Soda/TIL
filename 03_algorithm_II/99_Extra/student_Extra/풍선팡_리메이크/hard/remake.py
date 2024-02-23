import sys
sys.stdin = open("input.txt")
from copy import deepcopy

odd = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
even = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pang(i, j, is_odd):
    temp = arr[i][j]
    new_arr[i][j] = 0
    for di, dj in is_odd:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            temp += arr[ni][nj]
            new_arr[ni][nj] = 0
    return temp

def new_pang(i, j, is_odd):
    temp2 = new_arr[i][j]
    for di, dj in is_odd:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            temp2 += new_arr[ni][nj]
    return temp2

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    max_v = 0

    for i in range(N):
        for j in range(M):
            new_arr = deepcopy(arr)
            if arr[i][j] % 2 == 0:
                temp = max(max_v, pang(i, j, even))
                if temp % 2 == 0:
                    max_v2 = 0
                    for k in range(N):
                        for l in range(M):
                            if new_arr[k][l] % 2 == 0 and new_arr[k][l] > 0:
                                max_v2 = max(max_v2, new_pang(k, l, even))
                            elif new_arr[k][l] % 2 == 1:
                                max_v2 = max(max_v2, new_pang(k, l, odd))
                    max_sum = max(max_sum, max_v + max_v2)
                else:
                    max_v = max(max_v, temp)
            else:
                temp = max(max_v, pang(i, j, odd))
                if temp % 2 != 0:
                    max_v2 = 0
                    for k in range(N):
                        for l in range(M):
                            if new_arr[k][l] % 2 == 0 and new_arr[k][l] > 0:
                                max_v2 = max(max_v2, new_pang(k, l, even))
                            elif new_arr[k][l] % 2 == 1:
                                max_v2 = max(max_v2, new_pang(k, l, odd))
                    max_v = max(max_sum, max_v + max_v2)
                else:
                    max_v = max(max_v, temp)
                

    print(f'#{tc+1}', max_sum)