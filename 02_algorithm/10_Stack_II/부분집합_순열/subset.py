# backtrack을 이용하여 powerset을 구하는 함수
# a: 선택된 요소들의 배열 / k: 현재까지 선택된 요소의 개수 / input: 전체 요소의 개수
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES    # c: 후보 요소들을 저장하는 배열

    # 선택된 요소의 개수 == 전체 요소의 개수 -> process_solution 함수로 해를 처리
    if k == input:
        process_solution(a, k)
    # 선택된 요소의 개수 != 전체 요소의 개수 -> 선택된 요소의 개수 +1, 다음 후보 요소 생성
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)

        # 생성된 후보 요소들을 반복하여 선택, 해당 후보를 선택했을 때의 상태로 백트래킹 수행
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

# 선택된 요소의 상태에 따라 후보 요소 생성
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2    # MAXCANDIDATES: 후보 요소의 최대 개수
NMAX = 4             # NMAX: 전체 요소의 최대 개수
a = [0] * NMAX       # 초기 선택 요소들을 저장할 배열
backtrack(a, 0, 3)   # powerset 구하기