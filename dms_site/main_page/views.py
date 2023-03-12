from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import request
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView

from dms_site.servises import get_user_adventure, update_user_first_name
from dms_site.utils import Mixin
from .models import *
from .forms import CreationForm, UserChangePassword, UserChangeAccount


class MainPage(Mixin, ListView, LoginView):
    model = HomePost
    form_class = AuthenticationForm
    template_name = 'main_page/main_page.html'
    context_object_name = 'posts'

    def get_success_url(self):
        return reverse_lazy('main_page')

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)


class Registration(CreateView):
    model = User
    form_class = CreationForm
    template_name = 'main_page/register_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_page')


def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def user_account(request, username):
    if request.method == 'POST':
        form = UserChangeAccount(request.POST, instance=request.user)
        if form.is_valid():
            update_user_first_name(request, form['first_name'].value())
            return redirect('main_page')
    else:
        if request.user.username == username:
            user_adventure = get_user_adventure(request)
            form = UserChangeAccount()
            context = {
                "form": form,
                "adventure": user_adventure,
            }
            return render(request, "main_page/account.html", context)
        else:
            return render(request, "main_page")

    return redirect('main_page')


class UserPasswordChangeView(PasswordChangeView):
    """
    Изменение пароля пользователя
    """
    form_class = UserChangePassword
    template_name = 'main_page/change_password.html'
    success_message = 'Ваш пароль был успешно изменён!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('user_account', kwargs={'username': self.request.user.username})




