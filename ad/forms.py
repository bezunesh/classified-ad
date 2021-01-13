from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from .models import Post

def addCssFormControl(form):
    for field in form.fields:
       form.fields[field].widget.attrs.update({'class': 'form-control'})
        
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)
        
        self.fields['address'].widget.attrs.update({'placeholder': '1234 Main St, Alexandira, VA'})
        self.fields['phone'].widget.attrs.update({'placeholder': '(703) 444 7687'})
        self.fields['email'].widget.attrs.update({'placeholder': 'you@example.com'})
    class Meta:
        model = Post 
        fields = ['category', 'title', 'description', 'address', 'email', 'phone', 'author']

class SignupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
            
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)

class PwdChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)

class PwdResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)

class SetPwdForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)        