import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    ans = -1

    for i in range(int(N**(1/3)-1), int(N**(1/3)+2)):
        if i**3 == N:
            ans = i; break

    print(f'#{tc+1} {ans}')