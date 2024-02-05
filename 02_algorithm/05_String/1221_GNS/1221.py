# 1221 GNS

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    # 테스트 케이스 길이
    t_len = input()
    # 테스트 케이스
    str_num = input().split()
    # 숫자 대조 배열
    my_list = ["ZRO", "ONE", "TWO", "THR", "FOR",
               "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 문자 -> 숫자
    str_num = list(map(lambda x: my_list.index(x), str_num))
    # 정렬
    str_num.sort()
    # 숫자 -> 문자
    str_num = list(map(lambda x: my_list[x], str_num))
    
    print(f'#{tc+1}')
    print(*str_num)
