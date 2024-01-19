import requests
from pprint import pprint as print
dummy_data = list()

for idx in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{idx}'
    response = requests.get(API_URL)
    parsed_data = response.json()

    dummy_dict = {
        'company': parsed_data['company']['name'],
        'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'],
        'name': parsed_data['name'],
    }
    dummy_data.append(dummy_dict)

print(dummy_data)