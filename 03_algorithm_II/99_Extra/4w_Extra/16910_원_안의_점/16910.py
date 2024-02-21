import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N = int(input())

    sum_v = 4 * N + 1
    temp = 0
    for i in range(1, N):  # 세로
        circle = (N**2 - i**2) ** 0.5
        for j in range(1, N):  # 가로
            if j <= circle:
                temp += 1
    sum_v += temp * 4

    print(f'#{tc+1}', sum_v)
