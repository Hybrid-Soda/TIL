# 아래 함수를 수정하시오.
def count_character(string, alpbt):
    count = 0
    for i in string:
        if i == alpbt:
            count += 1
    return count


result = count_character("Hello, World!", "o")
print(result)  # 2
