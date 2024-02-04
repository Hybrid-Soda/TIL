# 연습문제 3

N = 5
arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]
one_d_arr = []
for i in range(5):
    one_d_arr.extend(arr[i])

# 카운팅 정렬
N = len(one_d_arr)
K = max(one_d_arr)
sort_one_d_arr = [0] * N
count = [0] * (K+1)

for num in one_d_arr:
    count[num] += 1

for i in range(K):
    count[i+1] += count[i]

for i in range(N-1,-1,-1):
    count[one_d_arr[i]] -= 1
    sort_one_d_arr[count[one_d_arr[i]]] = one_d_arr[i]

numbers = sort_one_d_arr

#    우  하  좌  상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
nj = 0
i, j = 0, 0

N = 5

snail = [[0] * N for _ in range(N)]

for num in numbers:
    # 현재 위치에 숫자 채우기
    snail[i][j] = num

    # 다음 위치 계산
    next_row, next_col = i + di[nj], j + dj[nj]

    # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향 변경
    if (
        next_row < 0 or next_row >= N or
        next_col < 0 or next_col >= N or
        snail[next_row][next_col]
    ):
        nj = (nj+1) % 4
        next_row, next_col = i + di[nj], j + dj[nj]
    
    # 다음 위치로 이동
    i, j = next_row, next_col

for i in range(N):
    print(snail[i])