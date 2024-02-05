# 2005 파스칼의 삼각형

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
