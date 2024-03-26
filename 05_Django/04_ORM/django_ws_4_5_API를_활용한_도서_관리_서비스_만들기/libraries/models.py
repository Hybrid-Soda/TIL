from django.db import models
import requests
from pprint import pprint

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'api_key'
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': 10,
            'start' : 1,
            'SearchTarget': 'Book',
            'output' : 'js',
            'Version' : '20131101'
        }
        response = requests.get(API_URL, params=params).json()

        for item in response['item']:
            my_model = Book(
                isbn = item['isbn'],
                author = item['author'],
                title = item['title'],
                category_name = item['categoryName'],
                category_id = item['categoryId'],
                price = item['priceSales'],
                fixed_price = item['fixedPrice'],
                pub_date = item['pubDate'],
            )
            my_model.save()