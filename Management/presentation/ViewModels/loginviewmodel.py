from django import forms
class LoginForm(forms.Form):
    UserName=forms.CharField(max_length=30)
    Password = forms.CharField(widget=forms.PasswordInput())