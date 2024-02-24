import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())  # 가로, 세로
n = int(input())  # 상점 개수
store = [list(map(int, input().split())) for _ in range(n)]  # 상점 위치 (방향, 인덱스)
d, i = map(int, input().split())  # 동근 위치
