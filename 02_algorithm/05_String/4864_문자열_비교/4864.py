# 4864 문자열 비교
# 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    str1 = input()
    str2 = input()
    ans = 0

    # str2에 str1이 있는지 체크
    if str1 in str2: ans = 1

    print(f'#{tc+1} {ans}')