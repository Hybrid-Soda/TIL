# 순차적 더하기 함수
def recur_example(number):
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)

result_1 = recur_example(5)
print(result_1)

# 거듭 제곱 재귀 함수
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return 2 * power(base, exponent - 1)

result_2 = power(2, 3)
print(result_2)

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    remain = number % 10
    quotient = number // 10
    if number < 10:
        return number
    else:
        return remain + sum_of_digits(quotient)

result_3 = sum_of_digits(321)
print(result_3)
