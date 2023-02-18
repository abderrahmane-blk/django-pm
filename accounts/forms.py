from django.contrib.auth.forms import AuthenticationForm
from django import forms 


must_attributes={"class" : "form-control"}

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args: any, **kwargs: any) -> None:
        super(UserLoginForm ,self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="username",
        widget = forms.TextInput(attrs=must_attributes)
    )
    password = forms.CharField(
        label="password",
        widget = forms.PasswordInput(attrs=must_attributes)
    )