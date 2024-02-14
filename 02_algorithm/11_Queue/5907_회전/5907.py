# 5907 회전

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())  # N: 숫자 개수 / M: 작업 횟수
    print(f'#{tc+1} {input().split()[M % N]}') # M % N: 몇 바퀴 돌고 남은 작업 횟수