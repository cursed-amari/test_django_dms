from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm

from dms_site.utils import Mixin

from .models import *
from .forms import *
from dms_site.servises import *


class AdventurePage(Mixin, ListView, LoginView):
    model = Adventure
    template_name = "adventure/adventure.html"
    context_object_name = "adventures"
    ordering = ['-time_update']
    paginate_by = 2

    def get_success_url(self):
        return reverse_lazy('adventure_page')


class AdventureCreate(LoginRequiredMixin, CreateView):
    model = Adventure
    form_class = CreateAdventure
    template_name = "adventure/adventure_create.html"
    login_url = reverse_lazy('adventure_page')

    def form_valid(self, form):
        form.save(commit=False)
        tit = slugify(translation_text_for_slug(form.cleaned_data['title']))
        form.instance.slug = tit
        form.instance.user = self.request.user
        sendTelegram(tit)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('adventure_page')


def adventure_post(request, slug):
    post = get_post(slug)
    form_class = AuthenticationForm()
    context = {
        "image": post.image.url,
        "title": post.title,
        "slug": post.slug,
        "username": post.user.username,
        "duration": post.duration,
        "amount_players": post.amount_players,
        "description": post.description,
        "file.url": post.file.url,
        "time_update": post.time_update,
        "adventure_count": user_adventure_count(request),
        "form": form_class
    }
    return render(request, "adventure/adventure_detail.html", context)


class UserProfileView(UpdateView):
    model = Adventure
    form_class = ChangeAdventure
    template_name = 'adventure/adventure_change.html'

    def get_success_url(self):
        return reverse_lazy('adventure_page')
