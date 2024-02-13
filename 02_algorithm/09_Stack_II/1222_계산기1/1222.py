import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    infix = input() # 중위 표기식
    postfix = ''    # 후위 표기식
    stack = []

    # 후위표기식으로 변환
    for char in infix:
        if char.isdecimal():
            postfix += char
        else:
            if not stack:
                stack.append(char)
            else:
                postfix += stack.pop()
                stack.append(char)
    postfix += stack.pop()

    # 변환식 계산
    for char in postfix:
        # 숫자면 stack에 저장
        if char.isdecimal():
            stack.append(char)
        # 연산자면 stack에서 두 숫자를 반환하여 더하고 저장
        else:
            stack.append(int(stack.pop()) + int(stack.pop()))

    # print(infix)
    # print(postfix)
    print(f'#{tc+1} {stack[0]}')