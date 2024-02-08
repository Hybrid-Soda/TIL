# 2005 파스칼의 삼각형

import sys
sys.stdin = open("input.txt")

# 팩토리얼 계산
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

# 각 줄의 조합 구해서 나열하는 함수
# if n=3 -> [3C3 3C2 3C1 3C0]
# nCr = n! / ((n-r)! * r!)
def combination(n):
    if n < 1:
        return [1]
    else:
        return [facto(n) // (facto(n-r) * facto(r)) for r in range(n+1)]

# 테스트 케이스
for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(N):
        print(*combination(i))

# --------------------------------------------
# 기가 맥힌 코드
# 한계 : 5까지만 가능
'''
for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(N):
        print(' '.join(str(11 ** i)))
'''
# --------------------------------------------
# 정석 DP 코드
sys.stdin = open("input.txt")

memo = [[1] * 10 for _ in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(N):
        print(*memo[i][:i+1])