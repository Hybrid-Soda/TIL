# 4839 이진탐색
# 이진 탐색 게임에서 이긴 사람 출력 (먼저 찾으면 승리)
# 계속 반으로 나누어 탐색 / 먼저 C에 도달하는 사람이 승리
# 종료 조건 : 한쪽이 먼저 C에 도달한 경우, 비긴 경우

import sys
sys.stdin = open('input.txt')

# 이진 탐색 재귀 함수
def binary_search(S, P, person):
    C = int((S + P)/2)
    # 값이 중앙 값보다 작으면, 배열의 왼쪽 반에서 탐색 반복
    if person < C:
        return 1 + binary_search(S, C, person)
    # 값이 중앙 값보다 크면, 배열의 오른쪽 반에서 탐색을 반복
    elif person > C:
        return 1 + binary_search(C, P, person)
    # 값이 중앙 값과 같으면, 값을 찾은 것이므로 재귀 함수 종료
    else:
        return 0

# 테스트 케이스 가동
for tc in range(int(input())):
    # P : 책의 전체 쪽수 / P_a, P_b : 두 사람이 찾을 쪽 번호
    P, P_a, P_b = map(int, input().split())

    # 이진 탐색 시작
    count_A, count_B = binary_search(1, P, P_a), binary_search(1, P, P_b)

    # 도출된 카운트 값으로 판단
    if count_A < count_B:
        ans = 'A'
    elif count_A > count_B:
        ans = 'B'
    else:
        ans = 0
    
    print(f'#{tc+1} {ans}')
