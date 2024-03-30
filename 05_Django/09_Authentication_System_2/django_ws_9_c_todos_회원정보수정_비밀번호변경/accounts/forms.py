from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email',)

'''
'email' field만 제공되도록 수정하지 않는 경우
Last login, Superuser status, Groups, User permissions, Staff status
등의 일반 사용자들이 접근해서는 안되는 정보들을 조작할 수 있게 된다
'''

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=12)
#     password = forms.CharField(widget=forms.PasswordInput())

