# 5656 벽돌 깨기

import sys
sys.stdin = open("input.txt")
from collections import deque

def play(board, score):
    return board, score

def DFS(board, score, n):
    nboard = [b[:] for b in board]

    for i in range(W):
        
        DFS(*play(nboard, score), n+1)
        pass

ds = ((-1, 0), (1, 0), (0, -1), (0, 1))

for tc in range(int(input())):
    N, W, H = map(int, input().split())  # 횟수, 열, 행
    board = [list(map(int, input().split())) for _ in range(H)]
    
    DFS(board, 0)

    exit()