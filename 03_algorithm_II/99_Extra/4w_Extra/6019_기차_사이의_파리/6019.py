import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 두 기차 전면부 사이 거리, A기차 속력, B기차 속력, 파리 속력
    D, A, B, F = map(int, input().split())
    T = D / (A + B)  # 기차 충돌까지 시간
    print(f'#{tc+1}', F*T)