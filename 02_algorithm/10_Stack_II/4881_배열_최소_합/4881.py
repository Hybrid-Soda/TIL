# 4881 배열 최소 합
# 목표 : 조건에 맞게 숫자를 골랐을 때의 최소 합을 출력
# 조건 : 행과 열이 겹치지 않도록 함

import sys
sys.stdin = open('input.txt')

def min_sum(i, N):
    global cnt
    global min_v
    cnt += 1
    # 모든 행을 탐색했다면, 도출된 순열을 통해 최소 합 구함
    if i == N:
        temp_sum = 0
        for j in range(N):
            temp_sum += arr[j][P[j]]
        min_v = min(min_v, temp_sum)
    # 모든 행을 탐색하지 않았다면, 인덱스를 바꾸고 다음 행의 
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            min_sum(i+1, N)
            P[i], P[j] = P[j], P[i]


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    cnt = 0
    min_sum(0, N)
    print(f'#{tc+1} {min_v} {cnt}')

# ------------------------------------------------------------------
'''
백트래킹 버전 (326 > 181 탐색시간이 대폭 감소)
'''
sys.stdin = open('input.txt')

def min_sum(i, N, temp_sum):
    global cnt
    global min_v
    cnt += 1
    # 모든 행을 탐색했다면, 도출된 순열을 통해 최소 합 구함
    if i == N:
        min_v = min(min_v, temp_sum)
    # 지금까지의 합이 최소 합 이상이라면 가능성이 없으므로 다른 순열로 탐색
    elif temp_sum >= min_v:
        return
    # 모든 행을 탐색하지 않았다면, 인덱스를 바꾸고 다음 행 탐색
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            min_sum(i+1, N, temp_sum+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    cnt = 0
    min_sum(0, N, 0)
    print(f'#{tc+1} {min_v} {cnt}')