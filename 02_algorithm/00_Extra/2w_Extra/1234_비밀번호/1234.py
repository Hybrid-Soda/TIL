# 1234 비밀번호

import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N, num_str = input().split()
    stack = []

    # 가공전 비밀번호 문자열 순회
    for txt in num_str:
        # 스택에 원소가 없으면 추가
        if not stack:
            stack.append(txt)
        # 스택에 원소가 있으면 현재 숫자와 이전 숫자 비교
        else:
            if txt == stack[-1]:
                stack.pop()
            else:
                stack.append(txt)

    print(f'#{tc+1} {"".join(stack)}')