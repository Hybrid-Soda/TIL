import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = input()
    Q = list(map(int, input().split()))
    m = min(Q) 

    # 5바퀴 돌 때마다 모든 수가 동일하게 감소 -> 따라서 1+2+3+4+5=15 를 나눠줌
    Q = [(x - (m // 15 - 1) * 15) for x in Q]
    idx = 0

    while True:
        # 한 사이클 진행
        for k in range(5):
            Q[(idx + k) % 8] -= k + 1
            # 0이하인 수가 나오면 종료
            if min(Q) <= 0:
                Q[Q.index(min(Q))] = 0
                break
        # 0이하인 수가 안 나오면 계속 진행
        else:
            idx += 5
            continue
        break

    # 0이 뒤로 갈 때까지 이동
    while Q[-1]:
        Q.append(Q.pop(0))

    print(f'#{T}', *Q)