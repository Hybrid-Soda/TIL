# 5099 피자 굽기
# 목표 : 화덕에 가장 마지막까지 남아있는 피자 번호 찾기

import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # N: 화덕 크기 / M: 피자 개수
    N, M = map(int, input().split())
    # 피자 번호와 치즈 양
    cheese = [[i+1, c] for i, c in enumerate(map(int, input().split()))]
    # 화덕 속 피자와 남은 피자
    oven = deque(cheese[:N])
    cheese = cheese[M-1:N-1:-1]

    while len(oven) > 1:
        pizza = oven.popleft()  # 피자 확인
        pizza[1] //= 2  # 남은 치즈 양

        # 치즈가 다 녹았으면 피자를 빼고 새로운 피자를 넣는다
        if pizza[1] == 0 and cheese:
            oven.append(cheese.pop())
        # 치즈가 다 녹지 않았으면 오븐에 다시 넣는다
        elif pizza[1] != 0:
            oven.append(pizza)

    print(f'#{tc+1} {oven.pop()[0]}')
