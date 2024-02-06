# 4869 종이붙이기
# 부분 -> 전체 : DP

import sys
sys.stdin = open('input.txt')

# 이전 케이스 + 이이전 케이스*2 = 현재 케이스
def attach_paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return 2*attach_paper(N-20) + attach_paper(N-10)

for tc in range(int(input())):
    print(f'#{tc+1} {attach_paper(int(input()))}')