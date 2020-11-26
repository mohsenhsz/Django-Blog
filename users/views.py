from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from django.contrib.auth import views as auth_views
from users.forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy


class UserRegisteration(auth_views.FormView):
    form_class = UserRegisterationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.create_user(form.cleaned_data)
        return super().form_valid(form)

    def create_user(self, data):
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password1'], )
        user.save()
        messages.success(self.request,
                        'Your account has been created! You are now able to log in',
                        'success')


class UserLogin(auth_views.LoginView):
    template_name = 'users/login.html'


class UserLogout(auth_views.LogoutView):
    template_name = 'users/logout.html'


class PasswordReset(auth_views.PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'users/email_template.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
