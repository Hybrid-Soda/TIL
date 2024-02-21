import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    wire = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0

     
    for i in range(N-1):
        for j in range(i+1, N):
            s1, e1 = wire[i]; s2, e2 = wire[j]
            # 교차하는 전선 체크
            if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
                cnt += 1

    print(f'#{tc+1}', cnt)