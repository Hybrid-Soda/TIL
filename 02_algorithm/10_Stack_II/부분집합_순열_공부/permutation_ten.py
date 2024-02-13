# def backtrack(a, k, n):
#     c = [0] * max_c

#     if k == n and sum(a[1:k+1]) == 10:
#         print(*a[1:k+1])
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, n)

# def construct_candidates(a, k, n, c):
#     in_perm = [False] * max_n
#     ncandidates = 0

#     for i in range(1, k):
#         in_perm[a[i]] = True

#     for i in range(1, n+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1

#     return ncandidates


# for i in range(1, 11):
#     max_c = i
#     max_n = i+1
#     a = [0] * max_n
#     backtrack(a, 0, i)


def backtrack(start=0, path=[], sum_left=10):
    # 원소의 합이 10이면 부분집합 출력 후 종료
    if sum_left == 0:
        print(path)
        return
    # 원소의 합이 10보다 크면 종료
    elif sum_left < 0:
        return
    # 원소의 합이 10보다 작으면 for문 실행
    elif sum_left > 0:
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]], sum_left - nums[i])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack()
