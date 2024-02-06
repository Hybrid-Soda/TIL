# 1289 초심자의 회문 검사

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    test_str = input()
    
    # 회문이면 1, 아니면 0 출력
    print(f'#{tc+1} {1 if test_str == test_str[::-1] else 0}')