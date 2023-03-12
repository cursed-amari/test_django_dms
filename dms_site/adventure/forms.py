from django.forms import ModelForm
from .models import Adventure


class CreateAdventure(ModelForm):
    class Meta:
        model = Adventure
        fields = ['title', 'slug', 'amount_players', 'duration', 'description', 'image', 'file', 'user']


class ChangeAdventure(ModelForm):
    class Meta:
        model = Adventure
        fields = ['title', 'amount_players', 'duration', 'description', 'image', 'file']

