import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    Q, dist = deque([N]), [0] * 1000001

    # 숫자 M에 도달하면 종료
    while not dist[M]:
        now = Q.popleft()

        # 총 4가지 경로 순회
        for next in [now+1, now-1, now*2, now-10]:
            # 범위를 만족하며 방문하지 않은 곳이라면 큐에 추가
            if 0 < next < 1000001 and not dist[next]:
                dist[next] = dist[now] + 1
                Q.append(next)

    print(f'#{tc+1} {dist[M]}')