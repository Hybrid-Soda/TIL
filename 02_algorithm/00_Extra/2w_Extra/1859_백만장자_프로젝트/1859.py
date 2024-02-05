# 1859 백만장자 프로젝트

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    prices = list(map(int, input().split()))
    max_price, profit = 0, 0

    # 뒤에서부터 탐색 - 부분 최대값에서 뺀 가격이 이익
    for price in prices[::-1]:
        max_price = max(max_price, price)
        profit += max_price - price
    
    print(f'#{tc+1} {profit}')