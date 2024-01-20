# 아래 함수를 수정하시오.
def even_elements(my_list):
    for i in range(len(my_list)):
        pop_num = my_list.pop(0)
        if pop_num % 2 == 0:
            my_list.extend([pop_num])
        
    return my_list
    

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
