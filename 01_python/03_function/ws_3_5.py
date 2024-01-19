number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]


def create_user(name, age):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    print(f'{user_info["name"]}님 환영합니다!')
    return user_info


def decrease_book(number):
    global number_of_book
    number_of_book -= number


def rental_book(info):
    number = info['age'] // 10
    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{info["name"]}님이 {number}권의 책을 대여하였습니다.')


many_user = list(map(create_user, name, age))
info = dict(map(lambda x: (x['name'], x['age']), many_user))

for user_name, user_age in info.items():
    rental_info = {'name': user_name, 'age': user_age}
