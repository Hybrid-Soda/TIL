# arr = [2,6,7,8,4,9,4,3,345,314,52]
# N = len(arr)

# def bubble_sort(arr, N):
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubble_sort(arr, N))


# arr = [2,6,3,3,7,8,4,9,4,3,14,11,2,5,6,3,7,2,2,5]
# N = len(arr)
# M = max(arr)

# def counting_sort(arr, N, M):
#     # 카운트 배열 생성
#     count = [0] * (M+1)
    
#     # 카운트 배열 기록
#     for i in arr:
#         count[i] += 1
    
#     # 누적합 구하기
#     for i in range(1, M+1):
#         count[i] += count[i-1]


#     # 정렬 배열 생성 및 마지막 원소부터 정렬
#     sort_arr = [0] * N
#     for i in range(N-1, -1, -1):
#         count[arr[i]] -= 1
#         sort_arr[count[arr[i]]] = arr[i]

#     return sort_arr

# print(counting_sort(arr, N, M))


# arr = [2,6,3,3,7,8,4,9,4,3,14,11,2,5,6,3,7,2,2,5]
# N = len(arr)

# def selection_sort(arr, N):
#     for i in range(N-1):
#         min_idx = i
#         for j in range(i+1, N):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

#     return arr

# print(select_sort(arr, N))

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'

# print(s1 == s2)
# print(s1 is s2)
# print(s1 == s3)
# print(s1 is s3)
# print(s1 == s4)
# print(s1 is s4)
# print(s1 == s5)
# print(s1 is s5)

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

s = '123'
a = atoi(s)
print(a+1)