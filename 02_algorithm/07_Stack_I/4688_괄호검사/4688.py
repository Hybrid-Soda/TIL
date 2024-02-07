# 4688 괄호검사

import sys
sys.stdin = open('input.txt')

''' 스택 사용한 코드 '''
for tc in range(int(input())):
    code = list(input())
    stack = []
    ans = 0

    # 주어진 코드 순회
    for char in code:
        # stack에 원소가 있을때
        if not stack:
            if char in ['{', '(']:
                stack.append(char)
            elif char in ['}', ')']:
                stack.append(char)
                break
        # stack에 원소가 없을때
        else:
            if char in ['{', '(']:
                stack.append(char)
            elif char in ['}', ')']:
                if (stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')'):
                    stack.pop()
                else:
                    break

    # 남은 괄호가 없으면 1, 있으면 0 출력
    print(f'#{tc + 1} {0 if stack else 1}')


''' 스택 사용하지 않은 코드 '''
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