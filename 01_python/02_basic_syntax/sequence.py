        #   0     1    2     3
my_list = ['가', '나', '다', '라']

# 인덱싱
print(my_list[1])

# 슬라이싱 - 범위가 벗어나도 out of range 가 발생하지 않는다
# 할 수 있는 것과 해도 되는 것은 다르다
# 슬라이싱으로 범위가 벗어난 경우,
# 예외 처리가 되지 않아서 예상하지 못한 문제가 발생 할 수 있다.
print(my_list[2:4])
print(my_list[:3])
print(my_list[3:])
print(my_list[0:5:2])
print(my_list[::-1])

# 길이
print(len(my_list))