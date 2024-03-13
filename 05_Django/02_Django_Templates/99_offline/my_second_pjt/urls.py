"""
URL configuration for my_second_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # index/ 경로 요청에 대한 응답 처리 view 함수
    path('', views.index),
    path('index/', views.index),
    # URL에는 kebab case, python function는 snake case
    # URL에는 특수문자 사용안함, python 에서 '-' 는 마이너스 연산자입니다.
    path('dtl-practice/', views.dtl_pratice),
    # variable routing
    # 변수에 담긴 값을 사용할 view 함수에게 인자로 넘긴다.
    # path 함수 내부에서 profile 호출시
    # profile(request, username=username)
    path('<username>/profile/', views.profile),
    path('<int:num>/', views.numbers),
    # 정수만 허용한다.
    # path('kjd742388/', views.profile),
    # path('yoonr72/', views.profile),
    # path('tjd4025/', views.profile),
    # path('brianwogus/', views.profile),
]
