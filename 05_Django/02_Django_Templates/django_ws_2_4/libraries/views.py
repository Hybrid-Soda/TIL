import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'api_key'


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': 12,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(API_URL, params=params).json()
    result = []

    for item in response['item']:
        info = {
            'title': item['title'],
            'author': item['author'],
            'pubDate': item['pubDate'],
            'isbn': item['isbn'],
            'salesPoint' : item['salesPoint'],
            'bestDuration' : item['bestDuration'],
        }
        result.append(info)

    result.sort(key=lambda x: x['salesPoint'], reverse=True)

    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)