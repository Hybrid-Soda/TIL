# 4880 토너먼트 카드게임
# 목표 : N명이 학생들이 카드를 골랐을 때 1등 찾기
# 1. 인덱스를 반으로 나누기

import sys
sys.stdin = open('input.txt')

def rsp(p1, p2):
    if card[p1] == card[p2]:
        return p1
    elif card[p1] - card[p2] == 1 or card[p1] - card[p2] == -2:
        return p1
    return p2


def divide(start, end):
    if start == end:
        return start

    p1 = divide(start, (start + end)//2)
    p2 = divide((start + end)//2 + 1, end)

    return rsp(p1, p2)


for tc in range(int(input())):
    N = int(input())
    # 1: 가위 / 2: 바위 / 3: 보
    card = list(map(int, input().split()))

    print(f'#{tc+1} {divide(0, N-1) + 1}')
