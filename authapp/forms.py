from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CiUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = CiUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = CiUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'
            field.help_text = ''
