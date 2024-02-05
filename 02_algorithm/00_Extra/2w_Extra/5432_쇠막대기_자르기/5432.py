# 5432 쇠막대기 자르기

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    sticks = input()   # 쇠막대기와 레이저 배치
    now_sticks = 0     # 현재 겹쳐진 쇠막대기 개수
    total_sticks = 0   # 잘려진 쇠막대기 개수

    for idx, txt in enumerate(sticks):
        # 여는 괄호이면 쇠막대기 시작 부분 or 레이저 부분
        if txt == '(':
            # 쇠막대기 시작 부분이면 잘려진 쇠막대기 개수 +1, 현재 겹쳐진 쇠막대기 +1
            if sticks[idx+1] == '(':
                now_sticks += 1
                total_sticks += 1
        # 닫는 괄호이면 쇠막대기 종료 부분 or 레이저 부분
        else:
            # 레이저 부분이면 현재 겹쳐진 쇠막대기 만큼 개수 추가
            if sticks[idx-1] == '(':
                total_sticks += now_sticks
            # 쇠막대기 종료 부분이면 현재 겹쳐진 쇠막대기 개수 -1
            else:
                now_sticks -= 1

    print(f'#{tc+1} {total_sticks}')