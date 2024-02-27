import sys
sys.stdin = open('input.txt')

password = (
'0001101', '0011001', '0010011', '0111101', '0100011',
'0110001', '0101111', '0111011', '0110111', '0001011',
)

for tc in range(int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    # 암호 위치 검색
    row, col = 0, 0
    for i in range(N):
        for j in range(M-1, M//2, -1):
            if code[i][j] != '0':
                row, col = i, j
                break
        if col:
            break
    
    # 암호 해독
    decode = []
    for i in range(col, col-56, -7):
        decode.append(password.index(code[row][i-6:i+1]))
    
    # 암호 검증
    sum_v = sum(map(lambda p: p[1] * 3 if p[0] % 2 != 0 else p[1], enumerate(decode))) 

    print(f'#{tc+1}', sum(decode) if sum_v % 10 == 0 else 0)