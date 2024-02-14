# 5099 피자 굽기
# 목표 : 화덕에 가장 마지막까지 남아있는 피자 번호 찾기

import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # N: 화덕 크기 / M: 피자 개수
    N, M = map(int, input().split())
    # C: 각각의 피자에 뿌려진 치즈 양
    C = list(map(int, input().split()))
    # queue(화덕)에 크기만큼 피자를 넣어줌
    Q = deque(C[:N])

    # 피자가 1개 남을때까지 굽기
    while len(Q) > 1:
        # 피자 확인
        pizza = Q.popleft() // 2
        # 피자가 다 구워진게 있다면
        if pizza == 0:


    print(f'#{tc+1}')