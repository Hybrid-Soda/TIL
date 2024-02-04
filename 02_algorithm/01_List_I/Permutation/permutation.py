# 순열로 나오는 집합들
def perms(elmt, start=0):
    n = len(elmt)
    if start == n - 1:
        yield elmt.copy()
    else:
        for i in range(start, n):
            elmt[start], elmt[i] = elmt[i], elmt[start]
            yield from perms(elmt, start + 1)
            elmt[start], elmt[i] = elmt[i], elmt[start]

# 사용 예제
input_elements = [1, 2, 3]
result = list(perms(input_elements))

print(result)



# 순열 경우의 수 구하기
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    return factorial(n) // factorial(n - r)

# 5P2 계산
result = permutation(5, 2)

print(result)