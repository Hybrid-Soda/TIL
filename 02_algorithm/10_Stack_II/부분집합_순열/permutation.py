'''
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
'''

# {1,2,3}을 포함하는 모든 순열을 생성하는 함수
# a: 선택된 요소 배열 / k: 현재 선택된 요소 개수 / n: 전체 요소 개수
def backtrack(a, k, n):
    c = [0] * max_c   # c: 후보 요소 저장 배열

    # 순열 제작 완료 -> 출력
    if k == n:
        print(*a[1:k+1])
    # 순열 제작 미완료 -> 선택된 요소의 개수 +1, 다음 후보 요소 생성
    else:
        k += 1
        ncandidates = construct_candidates(a, k, n, c)

        # 생성된 후보 요소들을 반복하여 선택, 해당 후보를 선택했을 때의 상태로 백트래킹 수행
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, n)


# 후보 요소 생성 함수 (선택된 요소의 상태에 따라)
def construct_candidates(a, k, n, c):
    in_perm = [False] * max_n
    ncandidates = 0

    # 선택된 요소는 True 표시
    for i in range(1, k):
        in_perm[a[i]] = True

    # False 표시 요소 후보 요소 저장 배열에 추가
    for i in range(1, n+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    # 추가된 후보 요소 개수 반환
    return ncandidates


max_c = 3            # max_c: 후보 요소의 최대 개수
max_n = 4            # max_n: 전체 요소의 최대 개수
a = [0] * max_n      # 초기 선택 요소들을 저장할 배열
backtrack(a, 0, 3)   # powerset 구하기
