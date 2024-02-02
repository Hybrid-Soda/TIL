# 4871 그래프 경로

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    node_num, route_num = map(int, input().split())
    line = sorted([list(map(int, input().split())) for _ in range(route_num)])
    start, end = map(int, input().split())
    stack = [line[0]]

    # 출발 노드와 도착 노드가 연결되면 종료
    while stack[0][0] != start or stack[-1][-1] != end:
        if 

        # 블록 빼는 부분
        if stack[-1][-1] 

    # print(f'#{tc+1} {ans}')
