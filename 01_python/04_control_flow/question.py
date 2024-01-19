'''
함수의 매개변수에 패킹을 사용할 때
가변 인자로 받게 되면 튜플로 받는다

그런데 왜 변수에 패킹을 사용할 때
다수의 데이터를 받으면 리스트로 받는 이유는?
'''


def func(*args):
    print(args)
    print(type(args))
func(1, 2, 3, 4)


a, *b, c = [1, 2, 3, 4, 5]
print(b)
print(type(b))


'''
tuple
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable한 데이터
- 여러개의 데이터를 담을 수 있는 colletion

- 내부요소 변경불가 immutable

list
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable한 데이터
- 여러개의 데이터를 담을 수 있는 colletion

- 내부요소 변경가능 mutable
'''

# 변수에 값을 할당할 때의 기대값은
# 특정 데이터를 편하게 참조할 수 있는 기능
# 해당 데이터의 값을 변경하거나, 조작하거나, 활용하는 용도를 기대

# 반면 함수는 입력값에 따른 정확한 값을 기대함
# 함수가 하는 일에 대해서 항상 같은 입력값에 같은 출력값이 나와야함


print([1, 2, 3, 4, 5])
print(*[1, 2, 3, 4, 5]) # tuple로 변환 후 (,)를 기준으로 하나 씩 print
print(1, 2, 3, 4, 5)


'''
익명함수 정의 키워드 lambda
기명함수 정의 키워드 def

lambda는 코드 재사용 불가능
- 순회 가능한 어떤 데이터에 대해 각 요소들에 대해서만 같은 로직을 실행 해야할 때 사용

def 함수이름(파라미터):
    할일

lambda 파라미터: 할일
'''

def my_sum(num1, num2):
    return num1 + num2
result = my_sum(1, 2)

my_sum2 = lambda num1, num2: num1 + num2
result_2 = my_sum2(3, 4)

print(result, result_2)

a = [1, 2, 3]
b = [4, 5, 6]
result_3 = list(map(lambda x, y: x + y, a, b))
print(result_3)
