from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
     class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('first_name', 'last_name',)


class CustomUserAdminChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('is_staff',)