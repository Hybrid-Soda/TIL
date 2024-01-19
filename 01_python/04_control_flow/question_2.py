'''
빈 리스트에는 선언과 동시에 정보 저장 안됨
없는 인덱스에는 직접 할당 불가
my_list = []
my_list[0] = 3
print(my_list)

튜플도 마찬가지
my_tuple = ()
my_tuple[0] = 3
print(my_tuple)

딕셔너리에는 선언과 동시에 정보 저장 됨
없는 키값에 직접 할당 가능
my_dict = {}
my_dict['key'] = 3
print(my_dict)

시퀀스때문에 그런가봄
'''

# numbers = []
# numbers += [1]
# numbers.append(3)
# numbers.extends([4, 5, 6])
# print(numbers)

# 같은 기능 다른 코드
# 각 문자열을 모두 정수로 바꾸어 리스트에 담으시오
numbers_words = '1 2 3 4 5 6 7 8 9'

# 문자열을 순회하면서 정수로 형변환이 가능하면
# 혹은 공백이 아니면
# 정수로 형변환해서 리스트에 담는다
numbers = []

# 문자열이 가진 각 요소를 임시면수 char에 할당해서 순회
for char in numbers_words:
    # print(char)
    if char != ' ' and char.isnumeric():
        numbers.append(int(char))
print(numbers)

numbers = list(map(int, numbers_words.split()))
print(numbers)


numbers_words = [
    '1 2 3 4 5',
    '6 7 8 9 10',
    '11 12 13 14 15',
]

numbers = []
for words in numbers_words:
    conversion_list = list(map(int, words.split()))
    numbers.extend(conversion_list)
print(numbers)

# List comprehension의 maximum
numbers = [list(map(int, words.split())) for words in numbers_words]
print(numbers)
