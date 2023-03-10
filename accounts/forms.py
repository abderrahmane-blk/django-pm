from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm , UserChangeForm
from django import forms 
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

must_attributes={"class" : "form-control"}

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args: any, **kwargs: any) -> None:
        super(UserLoginForm ,self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_("username"),
        widget = forms.TextInput(attrs=must_attributes)
    )
    password = forms.CharField(
        label=_("password"),
        widget = forms.PasswordInput(attrs=must_attributes)
    )

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_("first name"),
        widget = forms.TextInput(attrs=must_attributes)
    )
    last_name = forms.CharField(
        label=_("last name"),
        widget = forms.TextInput(attrs=must_attributes)
    )

    username = forms.CharField(
        label=_("username"),
        widget = forms.TextInput(attrs=must_attributes)
    )

    email = forms.EmailField(
        label=_("email"),
        widget = forms.EmailInput(attrs=must_attributes)
    )

    password1 = forms.CharField(
        label=_("password"),
        strip =False,
        widget = forms.PasswordInput(attrs=must_attributes)
    )
    password2 = forms.CharField(
            label=_("confirm password"),
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
        labels ={
            'first_name' :_("first_name"),
            'last_name' :_("last_name"),
            'username' :_("username"),
            'email':_("email")

        }
        widgets ={
            'first_name':forms.TextInput(attrs=must_attributes),
            'last_name':forms.TextInput(attrs=must_attributes),
            'username':forms.TextInput(attrs=must_attributes),
            'email':forms.EmailInput(attrs=must_attributes)
        }


