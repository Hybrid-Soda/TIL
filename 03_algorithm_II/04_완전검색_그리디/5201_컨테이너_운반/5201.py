import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())  # 컨테이너, 트럭 개수
    box = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    cnt, j = 0, 0

    # 컨테이너를 순회하며 적재에 적합한 트럭 탐색
    for i in range(N):
        # 더 이상 고려할 트럭이 없으므로 종료
        if j == M: break
        # 트럭이 결정되면 화물 적재 후 다음 트럭 고려
        if box[i] <= truck[j]: cnt += box[i]; j += 1

    print(f'#{tc+1} {cnt}')