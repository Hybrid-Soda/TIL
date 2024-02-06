# 3143 가장 빠른 문자열 타이핑

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # A : 전체 문자 / B : 탐색 문자
    A, B = input().split()
    # 타이핑 횟수 = 전체 문자 길이 - 특정 문자열 개수 * (특정 문자열의 길이 -1)
    ans = len(A) - A.count(B) * (len(B)-1)
    print(f'#{tc+1} {ans}')

    '''
    시간 복잡도 = 3*N
    '''
    
    # 풀어보기
    # 브루트 포스
    # KMP 방식
    # 보이어무어 방식