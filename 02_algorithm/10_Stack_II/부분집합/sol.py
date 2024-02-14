'''
K = 탐색 대상이 된 원소 번호
result = 최종 결괏값 (부분집합을 구하기 위한 type(list))
cnt = 부분 집합의 합
'''

def powerset(K, result, cnt):
    global cnnt
    cnnt += 1
    if cnt > 10:
        return
    if K == N:
        if cnt == 10:
            print(result)
        return
    else:
        # K번째 원소 사용
        powerset(K+1, result+[arr[K]], cnt+arr[K])
        # K번째 원소 사용 x
        powerset(K+1, result, cnt)

N = 10
arr = list(range(1, 11))
cnnt = 0

powerset(0, [], 0)
print(cnnt)
