# 4864 문자열 비교
# 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램

import sys
sys.stdin = open("input.txt")

# Python 키워드 in 사용
for tc in range(int(input())):
    print(f'#{tc+1} {1 if input() in input() else 0}')


# 고지식한 패턴 검색 : brute-force
sys.stdin = open("input.txt")
def brute_force(pat, txt, M, N):
    # text 인덱스
    for i in range(N-M+1):
        # pattern 인덱스
        for j in range(M):
            # 일치하지 않으면 패턴 순회 종료
            if txt[i+j] != pat[j]:
                break
        # 일치하여 for문이 무사히 끝나면 1 반환
        else:
            return 1
    # 모두 일치하지 않아 무사히 끝나지 않으면 0 반환
    return 0

for tc in range(int(input())):
    pat = input(); txt = input()
    print(f'#{tc+1} {brute_force(pat, txt, len(pat), len(txt))}')


# KMP 알고리즘
sys.stdin = open("input.txt")
def KMP(pat, txt, M, N):
    # 앞에 동일한 패턴이 몇 번 나왔는지 체크
    def make_lps(pat, M):
        lps = [0] * M
        for idx in range(1, M):
            if pat[lps[idx-1]] == pat[idx]:
                lps[idx] = lps[idx-1] + 1
        lps.insert(0, -1)
        return lps

    lps = make_lps(pat, M)
    p_i = 0; t_i = 0
    while t_i < len(txt):
        if txt[t_i] != pat[p_i]:
            p_i = lps[p_i]
        t_i += 1
        p_i += 1

        if p_i == len(pat):
            return 1
    return 0

for tc in range(int(input())):
    pat = input(); txt = input()
    print(f'#{tc+1} {KMP(pat, txt, len(pat), len(txt))}')


# 보이어 무어 알고리즘 - 수정 필요
sys.stdin = open("input.txt")
def boyer_moore(pat, txt, M, N):
    lps = {pat[i]: M-1-i for i in range(M)}
    p_i = M
    t_i = 0

    # text 인덱스
    while t_i <= N - p_i:
        # pattern 인덱스
        for p_idx in range(p_i-1, -1, -1):
            if txt[t_i + p_idx] != pat[p_idx]:
                t_i += lps.get(txt[t_i + p_idx], M)
                break # 틀리면 p_idx가 다시 M-1 되도록 조사종료
        else:
            return 1
    return 0

for tc in range(int(input())):
    pat = input(); txt = input()
    print(f'#{tc+1} {boyer_moore(pat, txt, len(pat), len(txt))}')
