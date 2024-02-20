import sys
sys.stdin = open('input.txt')
import heapq

for tc in range(int(input())):
    Q = []; sum = 0
    N = int(input())

    for n in map(int, input().split()):  # 힙에 저장
        heapq.heappush(Q, n)
    
    while N > 1:  # 조상 노드 값 합산
        N //= 2
        sum += Q[N-1]

    print(f'#{tc+1}', sum)