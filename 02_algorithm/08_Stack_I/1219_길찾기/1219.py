# 1219 길찾기


import sys
sys.stdin = open('input.txt')

for tc in range(10):
    test_case, route_num = map(int, input().split())
    route_list = list(map(int, input().split()))
    route_1 = [-1] * 100
    route_2 = [-1] * 100
    stack = [0]
    is_exist = 0

    # 루트를 정적배열에 저장 / index : 출발점 / value : 도착점
    for city in range(0, route_num*2, 2):
        if route_1[route_list[city]] == -1:
            route_1[route_list[city]] = route_list[city+1]
        else:
            route_2[route_list[city]] = route_list[city+1]

    # 깊이 우선 탐색 DFS - 스택이 비면 종료
    while stack:
        # 도착점 99에 도착하면 종료
        if stack[-1] == 99:
            is_exist = 1
            break

        arrive_1 = route_1[stack[-1]] 
        arrive_2 = route_2[stack[-1]]

        # 현재점과 이어진 다음 점이 갔던 곳이 아니라면 현재점에 -1 표시 후 그 점으로 이동
        if arrive_1 != -1:
            route_1[stack[-1]] = -1
            stack.append(arrive_1)
        elif arrive_2 != -1:
            route_2[stack[-1]] = -1
            stack.append(arrive_2)
        # 현재점과 이어진 다음 점이 갔던 곳라면 이전점으로 이동
        else:
            stack.pop()

    print(f'#{test_case} {is_exist}')