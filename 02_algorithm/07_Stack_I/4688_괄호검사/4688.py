# 4688 괄호검사

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    code = list(input())
    sample = ''

    # code에서 괄호만 sample에 옮기기
    for txt in code:
        if (txt == '{' or txt == '(' or
            txt == '}' or txt == ')'):
            sample += txt
    
    # 닫힌 괄호들은 모두 제거
    while sample:
        if '{}' in sample:
            sample = sample.replace('{}', '')
        elif '()' in sample:
            sample = sample.replace('()', '')
        else:
            break

    # 남은 괄호가 없으면 1, 있으면 0 출력
    print(f'#{tc+1} {1 if not sample else 0}')