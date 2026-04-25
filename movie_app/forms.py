from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Comment

User = get_user_model()

class RegisrtationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username',
                  'email','password1','password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['user_name','password']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Напишите комментарий...'})
        }