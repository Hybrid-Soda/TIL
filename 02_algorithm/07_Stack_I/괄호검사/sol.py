import sys
sys.stdin = open('input.txt')

'''
class를 활용한 stack 구현
'''

# stack 생성 시 크기를 지정해야 함
# 예상가능한 범주 내의 크기만큼 메모리 할당
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
            raise IndexError
        else:
            # top_value = self.data[self.top]
            # self.data[self.top] = None
            self.top -= 1                   # top 위치 1 감소
            # return top_value
            return self.data[self.top + 1]
    
    # top번째의 요소 출력
    def get(self):
        return self.data[self.top]
    
    # instance를 print 했을 때, stack의 data들을 바로 출력
    def __str__(self):
        return f'{self.data}'
    
    # top이 -1을 가리키면 stack은 비었다
    def is_empty(self):
        return self.top == -1
    
    # top이 size-1을 가리키면 stack은 꽉찼다
    def is_full(self):
        return self.top == self.size - 1


# print('----스택 생성----')
# stack = Stack(10)
# print(stack)

# print('----스택에 10 추가----')
# stack.push(10)
# print(stack)

# print('----스택 top 요소 출력----')
# print(stack.get())

# print('----스택 top 요소 제거----')
# print(stack.pop())
# print(stack)
# print(stack.top)

# print('----stack의 빔과 참----')
# for i in range(11):
#     stack.push(10)
# print(stack)
# print(stack.top)

# for i in range(11):
#     stack.pop()
# print(stack)
# print(stack.top)
    
for tc in range(int(input())):
    bracket = input()
    stack = Stack(100)
    result = True

    for char in bracket:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                result = False
                break

    if not stack.is_empty():
        result = False
    else:
        result = True
    
    print(f'#{tc+1} {result}')