import sys
sys.stdin = open('input.txt')

# 계산 함수
def cal(now):
    if len(tree[now]) == 4:
        oper = tree[now][1]          # 연산자
        a1 = cal(int(tree[now][2]))  # 왼쪽 자식 값
        a2 = cal(int(tree[now][3]))  # 오른쪽 자식 값

        if oper == '+': return a1 + a2    # 덧셈
        elif oper == '-': return a1 - a2  # 뺄셈
        elif oper == '*': return a1 * a2  # 곱셈
        elif oper == '/': return a1 / a2  # 나눗셈
    else:
        return int(tree[now][1])

# 메인
for tc in range(10):
    tree = [None] + [input().split() for _ in range(int(input()))]
    print(f'#{tc+1}', int(cal(1)))