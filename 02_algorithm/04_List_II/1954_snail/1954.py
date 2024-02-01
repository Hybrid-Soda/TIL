# 1954 달팽이 숫자

T = int(input())

for case in range(1, T+1):
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

    print(f'#{case}')
    for num in range(N):
        print(*snail[num])
