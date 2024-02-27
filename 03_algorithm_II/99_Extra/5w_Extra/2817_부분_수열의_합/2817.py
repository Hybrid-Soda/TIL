import sys
sys.stdin = open('input.txt')

def f(i, sum_v):
    if sum_v > K: return
    elif sum_v == K: global cnt; cnt += 1; return
    if i < N: f(i+1, sum_v+A[i]); f(i+1, sum_v)
 
for tc in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0; f(0, 0)
    print(f'#{tc+1} {cnt}')