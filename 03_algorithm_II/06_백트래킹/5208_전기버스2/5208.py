import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, *stop = list(map(int, input().split()))
    p, cnt = 0, -1

    while p < N - 1:
        max_r = 0
        for i in range(p + 1, p + stop[p] + 1):
            if N-1 == i:
                p = i; break
            if i + stop[i] > max_r:
                max_r = i + stop[i]
                p = i
        cnt += 1

    print(f"#{tc+1}", cnt)
