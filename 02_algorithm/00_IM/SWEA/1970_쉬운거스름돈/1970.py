import sys
sys.stdin = open('input.txt')

money = (50000, 10000, 5000, 1000, 500, 100, 50, 10)

for tc in range(int(input())):
    print(f"#{tc+1}")
    N = int(input())

    for i in range(8):
        print(N // money[i], end=' ')
        N %= money[i]
    print()