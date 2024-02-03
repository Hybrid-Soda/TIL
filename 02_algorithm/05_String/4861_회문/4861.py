# 4861 회문
# 회문 : 어느 방향에서 읽어도 같은 문자열
# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력

import sys
sys.stdin = open("input.txt")


def test(words1, words2, N, M):
    # 글자판 탐색 / 한 열안에서 고정 길이의 검색기가 이동하는 방식
    for i in range(N):
        for j in range(N-M+1):
            test1 = words1[i][j:j+M]
            test2 = words2[i][j:j+M]
            
            # 회문 조건 체크 후 만족시 반환
            if test1 == test1[::-1]:
                return test1
            elif test2 == test2[::-1]:
                return test2
    

for tc in range(int(input())):
    # NxN : 글자판 크기 / M : 회문의 길이
    N, M = map(int, input().split())

    # 글자판과 회전시킨 글자판 / 이후 슬라이싱을 위한 전처리
    words1 = [list(input()) for _ in range(N)]
    words2 = list(zip(*words1))

    # 함수 실행 후 회문 반환
    palindrome = ''.join(test(words1, words2, N, M))

    # 회문 출력
    print(f'#{tc+1}', palindrome)