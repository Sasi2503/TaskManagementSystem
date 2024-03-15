import re
from django import forms
from Management.DAL.Entities import Users



def passwordValidator(password):
    regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    if not re.match(regex, password):
        raise forms.ValidationError("Password must be at least 8 characters long and contain at least one letter, one number, and one special character.")

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    UserName = forms.CharField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput(), validators=[passwordValidator])

    def clean_UserName(self):
        username = self.cleaned_data.get('UserName')
        if Users.objects.filter(UserName=username).exists():
            raise forms.ValidationError("Username already exists, please  try another one.")
        return username

