from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    '''
        render 함수의 2번째 인자 template_name은
        templates/ 이전 경로는 모두 생략되어있다.

        -> 상대경로기는 한데,
        templates 폴더부터를 기준으로 상대경로이다.

        C:/users/ssafy/desktop/lectures/05_django/03_model/99_offline/articles/templates/
    '''
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)