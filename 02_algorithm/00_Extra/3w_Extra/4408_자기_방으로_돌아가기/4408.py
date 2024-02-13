# 4408 자기 방으로 돌아가기
# 목표 : 학생들이 이동하는 단위시간의 최솟값 구하기

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    room = [tuple(sorted(map(int, input().split()))) for _ in range(int(input()))]
    corridor = [0] * 201

    # 복도에서 겹치는 동선 체크
    for r in room:
        start = (r[0] + 1) // 2
        end = (r[1] + 1) // 2

        # 동선만큼 카운트
        for i in range(start, end+1):
            corridor[i] += 1

    # 제일 많이 겹치는 동선이 걸린 시간
    print(f'#{tc+1} {max(corridor)}')