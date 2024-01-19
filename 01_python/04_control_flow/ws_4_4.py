import requests
from pprint import pprint as print
dummy_data = list()

for idx in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{idx}'
    response = requests.get(API_URL)
    parsed_data = response.json()

    dummy_dict = {
        'company': parsed_data['company']['name'],
        'name': parsed_data['name'],
    }
    dummy_data.append(dummy_dict)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user():
    censored_user_list = dict()

    for idx in range(len(dummy_data)):
        company = dummy_data[idx]['company']
        name = dummy_data[idx]['name']
        return_value = censorship(company, name)

        if return_value == True:
            censored_user_list[company] = [name]
    return censored_user_list


def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user())