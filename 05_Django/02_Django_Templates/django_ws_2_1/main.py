import requests
from pprint import pprint

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'api_key'
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': 50,
    'start' : 1,
    'SearchTarget': 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

response = requests.get(API_URL, params=params).json()

result = []

for item in response['item']:
    my_dict = {}
    my_dict['국제 표준 도서 번호'] = item['isbn']
    my_dict['저자'] = item['author']
    my_dict['제목'] = item['title']
    my_dict['출간일'] = item['pubDate']
    result.append(my_dict)

pprint(result)
