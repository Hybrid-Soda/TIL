# 아래 함수를 수정하시오.
def reverse_string(string):
    result = ''.join(reversed(string))
    return result


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
