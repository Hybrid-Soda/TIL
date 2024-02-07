# 1234 비밀번호

import sys
sys.stdin = open("input.txt")

class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size           # list를 사용하여 스택 구현
        self.top = -1                       # 초기값이 없으므로 top의 위치는 -1

    # stack에 값 삽입
    def push(self, item):
        if self.is_full():
            print('Stack is full!!')
        else:
            self.top += 1                   # top 위치 1 증가
            self.data[self.top] = item      # item을 data의 top위치에 삽입


    # stack에서 값 삭제후 반환
    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!')
        else:
            # top_value = self.data[self.top]
            # self.data[self.top] = None
            self.top -= 1                   # top 위치 1 감소
            # return top_value
            return self.data[self.top + 1]

    # top번째의 요소 출력
    def get(self):
        return self.data[self.top]

    # top이 -1을 가리키면 stack은 비었다
    def is_empty(self):
        return self.top == -1

    # top이 size-1을 가리키면 stack은 꽉찼다
    def is_full(self):
        return self.top == self.size - 1


for tc in range(10):
    N, num_str = input().split()
    stack = Stack(int(N))

    # 가공전 비밀번호 문자열 순회
    for char in num_str:
        # 스택에 원소가 없으면 추가
        if stack.is_empty():
            stack.push(char)
        # 스택에 원소가 있으면 현재 숫자와 이전 숫자 비교
        else:
            if char == stack.get():
                stack.pop()
            else:
                stack.push(char)

    print(f'#{tc+1} {"".join(stack.data[:stack.top+1])}')