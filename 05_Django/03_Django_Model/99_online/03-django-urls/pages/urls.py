from django.urls import path
# 명시적 상대경로 - 현재위치의 views를 import
from . import views

app_name = 'pages'
urlpatterns = [
    # path('index/', views.index, name='index'),
]