# 4836 색칠하기
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어짐
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하시오
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):

    # 색칠할 부분과 컬러를 배열에 저장
    colors = [list(map(int, input().split())) for _ in range(int(input()))]

    # 흰 도화지와 답 준비
    paper = [[0]*10 for _ in range(10)]
    ans = 0

    # 색칠 작업 순회
    for task in colors:
        # 색칠하기 위한 순회
        for i in range(task[0], task[2]+1):
            for j in range(task[1], task[3]+1):
                # 만약 빨간색이라면 1 더함
                if task[4] == 1:
                    paper[i][j] += 1
                # 만약 파란색이라면 2 더함
                else:
                    paper[i][j] += 2
                # 보라색(value = 3)만 골라 카운트
                if paper[i][j] == 3:
                    ans += 1
    
    # 정답 출력
    print(f'#{tc+1} {ans}')
