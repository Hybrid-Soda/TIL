# 4839 이진탐색
# 이진 탐색 게임에서 이긴 사람 출력 (먼저 찾으면 승리)
# 계속 반으로 나누어 탐색 / 먼저 C에 도달하는 사람이 승리
# 종료 조건 : C가 타겟값에 도달한 경우
# 입력값은 다르지만 프로세스는 같아서 함수 사용

import sys
sys.stdin = open('input.txt')

# 이진 탐색 재귀 함수
def binary_search(S, P, target_number):
    C = int((S + P)/2)

    # 값 < 중앙 값 : 배열의 왼쪽 부분 탐색 반복
    if target_number < C:
        return 1 + binary_search(S, C, target_number)
    # 값 > 중앙 값 : 배열의 오른쪽 부분 탐색 반복
    elif target_number > C:
        return 1 + binary_search(C, P, target_number)
    # 값 = 중앙 값 : 함수 종료
    else:
        return 0

# 테스트 케이스 가동
for tc in range(int(input())):
    # P : 책의 전체 쪽수 / P_a, P_b : 두 사람이 찾을 쪽 번호
    P, P_a, P_b = map(int, input().split())

    # 이진 탐색 시작
    count_A, count_B = binary_search(1, P, P_a), binary_search(1, P, P_b)

    # 판단
    if count_A < count_B:
        ans = 'A'
    elif count_A > count_B:
        ans = 'B'
    else:
        ans = 0
    
    print(f'#{tc+1} {ans}')
