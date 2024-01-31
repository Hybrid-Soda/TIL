# 4837 부분집합의 합
# 집합 A (1 ~ 12)의 부분집합 중 N개의 원소를 갖고, 원소의 합이 K인 부분집합의 개수를 출력
# 해당하는 부분집합이 없으면 0 출력 / 모든 부분집합을 만들어 답을 찾아도 가능

import sys
sys.stdin = open('input.txt')

# 집합 A 정의
A = list(range(1, 13))

for tc in range(int(input())):
    # N : 부분 집합 원소의 수 / K : 부분 집합의 합
    N, K = (map(int, input().split()))
    ans = 0

    # 집합 A의 부분 집합의 개수만큼 순회 / 각 순회마다 임시리스트 생성
    for i in range(1 << len(A)):
        part_set = []

        # 집합 A의 개수만큼 순회
        for j in range(len(A)):

            # i의 j번 비트가 1이라면 임시리스트에 A[j] 추가
            if i & (1 << j):
                part_set.append(A[j])
        
        # 임시 리스트가 N개의 원소를 갖고, 원소의 합이 K인 부분집합이라면 카운트
        if len(part_set) == N and sum(part_set) == K:
            ans += 1

    # 출력
    print(f'#{tc+1} {ans}')