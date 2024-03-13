from django.shortcuts import render

# Create your views here.
def index(request):
    # app에서 사용할 template은 templates 폴더에 넣는데
    # 왜... app/templates/app/*.html
    # 처럼 app 이름이 중복되도록 폴더 구조를 만들까?
    '''
        만약... templates/*.html 로 만들었다면...
        app이 2개인경우.. articles와 accounts에서...
        articles/templates/index.html
        accounts/templates/index.html

        두 파일 중... 순회 순서에 따라서 먼저 발견하는 대상
        index.html을 render 하게 되어버린다.

        그러면... 폴더를 그렇게 만들지말고...파일명을...
        articles/templates/article_index.html
        accounts/templates/account_index.html

        이렇게 만들면 되는거 아님?
        맞음!

        articles/templates/articles/...
        articles/templates/assets/...
        articles/templates/categories/...
    '''
    # template에 작성된 DTL 등은...
    # render에 의해서 올바른 HTML 모양을갖추고
    # 사용자에게 제공된다.
    return render(request, 'articles/index.html')

def dtl_pratice(request):
    lunch = ['타코야끼', '치킨하이라이스', '볶음우동', '강식당라면', '기사식당불백']
    empty_list = []
    context = {
        'lunch': lunch,
        'empty_list': empty_list
    }
    return render(request, 'articles/dtl_practice.html', context)

'''
    함수의 매개변수인데...
    그리고 url의 변수명인데..
    왜 두 개는 항상 동일해야 할까?
    왜 매개변수의 값이 고정되어야 할까?
    그런 경우가 함수 정의 할때 언제가 있지?

    def some(keyword=None):
        return keyword

    some(keyword=1)
'''
def profile(request, username):
    print('=='* 30)
    print(username)
    print('=='* 30)
    context = {
        'username': username
    }
    return render(request, 'articles/profile.html', context)

def numbers(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/numbers.html', context)