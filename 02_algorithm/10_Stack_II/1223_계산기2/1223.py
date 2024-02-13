import sys
sys.stdin = open('input.txt')

# 연산자 우선순위
prior = {'+': 1, '-': 1, '*': 2, '/': 2}

for tc in range(10):
    N = int(input())
    infix = input() # 중위 표기식
    postfix = ''    # 후위 표기식
    stack = []

    # 후위표기식으로 변환
    for char in infix:
        # 숫자면 String에 추가
        if char.isdecimal():
            postfix += char
        # 연산자면 stack에 넣어두고 조건에 따라 String에 추가
        else:
            if not stack:
                stack.append(char)
            elif prior[char] > prior[stack[-1]]:
                stack.append(char)
            elif prior[char] <= prior[stack[-1]]:
                while stack and prior[char] <= prior[stack[-1]]:
                    postfix += stack.pop()
                stack.append(char)
    while stack:
        postfix += stack.pop()

    # 변환식 계산
    for char in postfix:
        # 숫자면 stack에 저장
        if char.isdecimal(): stack.append(char)
        # 연산자면 stack에서 두 숫자를 반환하여 더하고 저장
        else:
            B = int(stack.pop()); A = int(stack.pop())
            if char == '+': stack.append(A + B)
            elif char == '-': stack.append(A - B)
            elif char == '*': stack.append(A * B)
            elif char == '/': stack.append(A / B)

    # print(infix)
    # print(postfix)
    print(f'#{tc+1} {stack[0]}')