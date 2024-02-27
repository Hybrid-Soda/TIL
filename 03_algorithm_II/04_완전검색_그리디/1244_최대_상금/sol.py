import sys
sys.stdin = open('input.txt')

def per(i, k):
    if i == N:
        global max_v
        max_v = max(max_v, int(''.join(num)))
        return
    if k < len(num):
        for j in range(0, len(num)-1):
            if k != j:
                num[k], num[j] = num[j], num[k]
                per(i+1, k+1)
                num[k], num[j] = num[j], num[k]

for tc in range(int(input())):
    num, N = input().split()
    num, N = list(num), int(N)
    max_v = 0; per(0, 0)
    print(f'#{tc+1} {max_v}')
