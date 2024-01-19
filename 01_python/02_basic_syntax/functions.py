# 리스트 다루는 연습
# '메서드' 라는 개념

def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2

# 함수를 호출한다
some_func('가', '나')

# 함수를 호출한 결과를 변수에 할당
answer = some_func(1, 2) # return 값이 없으면 Python이 알아서 None을 반환함
print(answer) # None : 값이 없음을 나타내기 위한 데이터 타입

# 리스트란 시퀀스 형태의 데이터
# 순서가 있는 값이고, 정렬되어 있음을 보장하지는 않는다.
# 내부 요소를 오름차순으로 정렬하고 싶다.
numbers = [4, 3, 2, 1]
# 메서드 : 누군가가 가지고 있는 함수
# 리스트가 가지고 있는 sort 메서드
result = numbers.sort() # 사용방법은 함수와 완전히 동일

# 내장함수 : 파이썬이 기본적으로 가지고 있는 함수
print(result)
print(numbers)
print("-------------------")

numbers = [4, 3, 2, 1]
# sorted 함수와 sort 메서드의 차이
# list.sort() 메서드는 정렬 대상인 주어(리스트)가 정해져 있다
# 반면, sorted 함수는 '누구를' '정렬'할 것인지 정해줘야 한다 -> 인자를 넘긴다
result = sorted(numbers)
print(result)
print(numbers)

# sorted 는 받은 인자는 수정하지 않은 채 return 만 한다

def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2
    return result

answer = some_func('연', '고')

print(answer + '전')

# 따라서 return 값을 직접 작성해주는 것이 좋으나
# 반환 할 필요가 없는 경우에는 굳이 안 써줘도 된다


def other_func(parm1, parm2):
    result = parm1 * parm2
    print(result, '-> 함수 내부에서 실행')
    return result
answer = other_func(2, 3)
print(answer, '-> 함수 외부에서 실행')

'''
def sorted(iterable, key=None, reverse=False):
    pass
sorted(list, True)
'''

print(sorted(numbers, reverse=True))


def some_func(name, age):
    pass

# some_func() got multiple values for argument 'name'
# some_func(3, name='홍')

some_func(age=3, name='홍')


def other_func(*args, name):
    pass

other_func(1, 2, 3, 4, 5, 6, 7, name='홍')


# -----------------------------------------------
a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c) # 10 2 500
    local(500)
    print(a, b, c) # 10 2 3
enclosed()
print(a, b) # 1 2
# print(c) # 많이 발생하는 오류에 속함 (name 'c' is not defined)

'''
Q. 함수를 왜 만들어야 함?
A. 같은 코드 다시 쓰지 말자
    추가로 단순히 반복되는 것 말고, input에 따라 같은 일을 하는데
    output이 달라지는 모든 경우에 대입하기 위해

Q. 알고리즘을 하는 이유
A. 특정 상황에 대한 문제 해결 능력
'''

global_var = 100
my_list = [1, 2, 3]

def local():
    # 글로벌 스코프의 변수 함수 내에서 출력
    print(global_var)
    # 글로벌 변수의 값을 로컬에서 변경할 수 없다
    # global_var = 3
    # print(global_var)
    # 리스트의 참조는 바꿀 수 있다
    my_list[0] = 100
    print(my_list)

local()

# 함수로 글로벌 스코프에 정의된 변수의 값을 바꾸는 법
# 가장 함수를 잘 쓰는 방법
global_var = 100
def local(parm):
    parm += 3
    return parm

global_var = local(global_var)
print(global_var)

# global 키워드만 사용 x
# 어느 시점에 global 변수가 바뀌었는지 파악하기 어려움
global_var = 100
def local():
    global global_var
    global_var += 3
local()
print(global_var)

