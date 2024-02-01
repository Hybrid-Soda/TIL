# 4871 그래프 경로
# 특정한 두 개의 노드가 연결되어 있는지 확인
# 경로가 있으면 1, 없으면 0을 출력
# 1. 간선 정보 순회 중 이전 뒤 숫자와 다음 앞 숫자가 같으면 연결 블록 추가
# 2. 그 다음 출발 노드와 도착 노드가 일치하면 종료 아니면 위 반복
# 3. 추가할 블록이 없으면 그 블록을 빼고 그 다음부터 순회해서 다른 블록 추가
# 4. 다른 블록도 없으면 다시 블록을 뺌
# 5. 마지막까지 순회했는데도 안되면 경로가 없는 것
# 블록 빼는 조건 : 추가할 블록 없으면
# 블록 넣는 조건 : 추가할 블록 있으면

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    # V : 노드 개수 / E : 간선 개수
    V, E = map(int, input().split())
    # 간선 정보
    line = sorted([list(map(int, input().split())) for _ in range(E)])
    # S : 출발 노드 / G : 도착 노드
    S, G = map(int, input().split())
    # 스택 초기화
    stack = [line[0]]

    # 출발 노드와 도착 노드가 연결되면 종료
    while stack[0][0] != S or stack[-1][-1] != G:
        if 

        # 블록 빼는 부분
        if stack[-1][-1] 

    # print(f'#{tc+1} {ans}')
