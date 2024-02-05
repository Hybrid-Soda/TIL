# 16268 풍선팡2
# 풍선이 NxM으로 있음
# 풍선을 터뜨리면 종이 꽃가루 개수만큼 상하좌우 풍선이 추가로 터짐
# 한 개의 풍선을 선택할 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 풍선 리스트 순회
    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            # 풍선 터뜨리기
            # 아래쪽 끝
            if i+1 < N:
                temp += arr[i+1][j]
            # 위쪽 끝
            if i-1 >= 0:
                temp += arr[i-1][j]
            # 오른쪽 끝
            if j+1 < M:
                temp += arr[i][j+1]
            # 왼쪽 끝
            if j-1 >= 0:
                temp += arr[i][j-1]
            ans = max(ans, temp)

    print(f'#{tc+1} {ans}')


# 델타 탐색 방법 풀이
sys.stdin = open('input.txt')
#    우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(int(input())):
    # NxM 크기의 게임판
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0   # 최대 꽃가루 합계
    
    for i in range(N):
        for j in range(M):
            # 터뜨린 풍선의 꽃가루 수
            cnt = arr[i][j]
            # 주변 풍선의 꽃가루 수
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                # 주어진 판을 넘어가지 않는 경우에만 카운트
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            
            # 꽃가루 최대값과 비교
            if max_v < cnt:
                max_v = cnt
    
    print(f'#{tc+1} {max_v}')