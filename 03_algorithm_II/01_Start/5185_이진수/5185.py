import sys
sys.stdin = open('input.txt')

hex_to_bin = {hex(idx)[2:].upper(): f'{idx:04b}' for idx in range(16)}

for tc in range(int(input())):
    N, N16 = input().split()
    print(f'#{tc+1}', end=' ')
    for char in N16:
        print(hex_to_bin[char], end='')
    print()