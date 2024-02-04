# 1954 달팽이 숫자

for tc in range(int(input())):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
    stock = 0

    # 회전 바퀴수 만큼 순회
    for j in range(N//2):
        # ahead : 한바퀴 돌때 각 라인이 진행할 길이 (2씩 누적해서 줄어듦)
        ahead = N-1-2*j

        # 각각 라인 진행
        for k in range(ahead):
            snail[j][k+j] = stock + (k+1)
            snail[k+j][-1-j] = stock + ahead + (k+1)
            snail[-1-j][-1-k-j] = stock + 2*ahead + (k+1)
            snail[-1-k-j][j] = stock + 3*ahead + (k+1)

        # stock : 한바퀴 돌았을 때 총 누적 길이 (각 라인 * 4)
        stock += 4*ahead

    # N이 홀수일 경우 마지막 한칸 채우기
    if N % 2 == 1:
        snail[N//2][N//2] = N**2

    print(f'#{tc+1}')
    for num in range(N):
        print(*snail[num])


'''
# 델타 탐색

for tc in range(int(input())):
    #    우  하  좌  상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    nj = 0
    i, j = 0, 0

    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    for num in range(1, N+1):
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

    print(f'#{tc+1}')
    for num in range(N):
        print(*snail[num])
'''
