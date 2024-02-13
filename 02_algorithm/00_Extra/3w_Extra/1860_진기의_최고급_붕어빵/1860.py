# 1860 진기의 최고급 붕어빵
# 목표 : 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M, K = map(int, input().split())  # N: 사람 수 / M: 제작 시간 / K: 단위 생산 개수
    time = sorted(list(map(int, input().split())))  # 고객 별 도착 시간
    fst = min(time)  # 최초 손님 도착 시간
    bread = fst//M*K  # 최초 손님 도착 전까지 만들어 둔 빵

    # 최초 손님 도착 시간 < 제작 시간 : 즉시 실패
    if fst < M:
        print(f'#{tc+1} Impossible')
        continue
    
    # 만들어 둔 빵 >= 사람 수 : 즉시 성공
    if bread >= N:
        print(f'#{tc+1} Possible')
        continue

    ans = 'Possible'
    for i in range(N):
        # 손님 도착 시 남아있는 붕어빵 재고
        stock = time[i]//M*K - (i+1)
        # 재고가 없다면 실패
        if stock < 0:
            ans = 'Impossible'
            break
    
    print(f'#{tc+1} {ans}')
