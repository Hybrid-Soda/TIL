from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
    
    is_completed = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False,
    )