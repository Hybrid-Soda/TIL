# 4873 반복문자 지우기
# 반복문자를 지운 후 남은 문자열의 길이를 출력

import sys
sys.stdin = open("input.txt")

# 스택 사용해서 푼 방법
for tc in range(int(input())):
    word = list(input())
    stack = []

    for i in word:
        # 스택이 비어있다면 문자 추가 / 아니면 다음 조건문
        if stack == []:
            stack.append(i)
        else:

            # 반복문자이면 제거 / 아니면 문자 추가
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    
    print(f'#{tc+1} {len(stack)}')

print('----------------')
sys.stdin = open("input.txt")

# 스택 없이 푼 방법
for tc in range(int(input())):
    string = list(input())
    idx = 0

    # 조사 인덱스가 최종 문자열 길이에 도달한다면 종료
    while idx < len(string)-1:
        
        # 반복문자이면 제거
        if string[idx] == string[idx+1]:
            string.pop(idx)
            string.pop(idx)
            # 처음 문자가 아니면 이전 글자로 돌아감
            if idx != 0:
                idx -= 1
        # 현재 글자와 다음 글자가 다르다면 다음 글자로 진행
        else:
            idx += 1

    print(f'#{tc+1} {len(string)}')
