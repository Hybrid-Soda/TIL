# 4843 특별한 정렬
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력
# 큰 수와 작은 수를 번갈아 정렬

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    sort_arr = []

    # 정렬된 배열의 뒤-앞의 숫자를 새로운 배열에 추가
    for i in range(5):
        sort_arr.append(arr.pop(-1))
        sort_arr.append(arr.pop(0))

    print(f'#{tc+1}', *sort_arr)