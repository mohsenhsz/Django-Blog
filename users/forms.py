from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError


class UserRegisterationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32,widget=forms.TextInput(
                               attrs={'class':'form-control', 'placeholder':'Your Username'})
                                )
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                             attrs={'placeholder':'Your Email'})
                             )
    password1 = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput(
                                attrs={'class':'form-control', 'placeholder':'Your password'})
                                )
    password2 = forms.CharField(label='Password Confirm', max_length=32, widget=forms.PasswordInput(
                                attrs={'class':'form-control', 'placeholder':'Your password'})
                                )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():  # if user != []:
            raise ValidationError('This email is early exist!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords are not match')
