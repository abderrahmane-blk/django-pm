from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm , UserChangeForm
from django import forms 
from django.contrib.auth.models import User


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

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label="first name",
        widget = forms.TextInput(attrs=must_attributes)
    )
    last_name = forms.CharField(
        label="last name",
        widget = forms.TextInput(attrs=must_attributes)
    )

    username = forms.CharField(
        label="username",
        widget = forms.TextInput(attrs=must_attributes)
    )

    email = forms.EmailField(
        label="email",
        widget = forms.EmailInput(attrs=must_attributes)
    )

    password1 = forms.CharField(
        label="password",
        strip =False,
        widget = forms.PasswordInput(attrs=must_attributes)
    )
    password2 = forms.CharField(
            label="confirm password",
            strip =False,
            widget = forms.PasswordInput(attrs=must_attributes)
        )

    class Meta(UserCreationForm.Meta):
        fields=('first_name','last_name','username','email')

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        widgets ={
            'first_name':forms.TextInput(attrs=must_attributes),
            'last_name':forms.TextInput(attrs=must_attributes),
            'username':forms.TextInput(attrs=must_attributes),
            'email':forms.EmailInput(attrs=must_attributes)
        }


