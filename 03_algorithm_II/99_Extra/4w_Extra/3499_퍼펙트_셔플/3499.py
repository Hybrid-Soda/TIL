import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    card = input().split()
    new_card = []

    if N % 2 == 0:
        for c in range(N//2):
            new_card.append(card[c])
            new_card.append(card[N//2+c])
    else:
        for c in range(N//2 + 1):
            new_card.append(card[c])
            if c < N//2: new_card.append(card[N//2+c+1])

    print(f'#{tc+1}', *new_card)