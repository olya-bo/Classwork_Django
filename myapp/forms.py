from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not age % 2:
            raise ValidationError('Age should be odd')
        return age

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        nickname = cleaned_data.get('nickname')
        if str(age) in nickname:
            self.add_error('age', 'Age cannot be in nickname')
        self.add_error(None, 'This form always incorrect')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError()

