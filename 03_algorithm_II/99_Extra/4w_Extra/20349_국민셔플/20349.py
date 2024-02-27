import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, T = map(int, input().split())
    card = [i for i in range(1, N+1)]
    L = int(0.63 * N) + 1

    for _ in range(T):
        card = card[L:] + card[:L]
        if N % 2 == 0: card = [card[i // 2] if i % 2 == 0 else card[N // 2 + i // 2] for i in range(N)]
        else: card = [card[i // 2] if i % 2 == 0 else card[N // 2 + (i + 1) // 2] for i in range(N)]

    print(f'#{tc+1}', *card)