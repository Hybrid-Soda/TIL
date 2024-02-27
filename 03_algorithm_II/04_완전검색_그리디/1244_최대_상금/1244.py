import sys
sys.stdin = open('input.txt')

def per(n):
    if n == N:
        global max_v
        max_v = max(max_v, int(''.join(num)))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            num[i], num[j] = num[j], num[i]
            char = int(''.join(num))
            if (n, char) not in visit:
                per(n+1)
                visit.append((n, char))
            num[i], num[j] = num[j], num[i]

for tc in range(int(input())):
    num, N = input().split()
    num, N = list(num), int(N)
    L, max_v = len(num), 0
    visit = []
    per(0)
    print(f'#{tc+1} {max_v}')
