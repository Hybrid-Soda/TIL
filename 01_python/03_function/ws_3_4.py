number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{user_info["name"]}님 환영합니다!')
    increase_user()
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = list(map(create_user, name, age, address))

print(user_list)