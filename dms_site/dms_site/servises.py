import requests

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from adventure.models import Adventure

from config import tg_token, tg_chat_id


def sendTelegram(title):
    token = tg_token
    chat_id = tg_chat_id
    text = f'Новое приключение \n {title}'
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text,
    })


def update_user_first_name(request, new_name):
    User.objects.get(username=request.user.username).update(first_name=new_name)


def get_post(slug):
    return get_object_or_404(Adventure, slug=slug)


def get_user_adventure(request):
    return Adventure.objects.filter(user_id=request.user.id)


def user_adventure_count(request):
    return Adventure.objects.filter(user_id=request.user.id).count()


def save_adventure_to_db(request):
    ad = Adventure(
        title=request.GET.get("title"),
        slug=translation_text_for_slug(request.GET.get("title")),
        amount_players=request.GET.get("amount_players"),
        duration=request.GET.get("duration"),
        description=request.GET.get("description"),
        image=request.GET.get("image"),
        file=request.FILES.get("file"),
        user=request.user
    )
    ad.save()


def translation_text_for_slug(string: str):
    if string:
        return string.translate(
            str.maketrans(
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSSY_.EUA"))

