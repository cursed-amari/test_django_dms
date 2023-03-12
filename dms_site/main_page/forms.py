from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _


class CreationForm(UserCreationForm):
    username = forms.CharField(max_length=20,
                                  validators=[RegexValidator(
                                    r"^[-a-zA-Z0-9_]+\Z",
                                    "Login должен быть не менее 3 и не более 20 символов состоять только из латинских символов и не содержать пробелов"),
                                      MaxLengthValidator(20),
                                      MinLengthValidator(3)])
    first_name = forms.CharField(max_length=20,
                                  validators=[RegexValidator(
                                    r"^[-a-zA-Z0-9_А-Яа-я]+\Z",
                                    "Name не должно быть не менее 3 и не более 20 символов и не содержать пробелов"),
                                      MaxLengthValidator(20),
                                      MinLengthValidator(3)])
    password1 = forms.CharField(label=_("Password"),
                                strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                help_text=password_validation.password_validators_help_text_html(),
                                validators=[RegexValidator(
                                    r"^[-a-zA-Z0-9_]+\Z",
                                    "Пароль должен состоять только из латинских символов и не содержать пробелов"),
                                      ])
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                strip=False,
                                help_text=_("Enter the same password as before, for verification."),
                                validators=[RegexValidator(
                                    r"^[-a-zA-Z0-9_]+\Z",
                                    "Пароль должен состоять только из латинских символов и не содержать пробелов"),
                                      ])

    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('username', 'first_name', 'password1', 'password2')


class UserChangePassword(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                    strip=False,
                                    help_text=password_validation.password_validators_help_text_html(),
                                    validators=[RegexValidator(
                                        r"^[-a-zA-Z0-9_]+\Z",
                                        "Пароль должен состоять только из латинских символов и не содержать пробелов"),
                                        MinLengthValidator(8,
                                                           'Пароль должен состоять только из латинских символов не содержать пробелов и быть более 8 символов')])
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    strip=False,
                                    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                    validators=[RegexValidator(
                                        r"^[-a-zA-Z0-9_]+\Z",
                                        "Пароль должен состоять только из латинских символов и не содержать пробелов"),
                                        MinLengthValidator(8,
                                                           'Пароль должен состоять только из латинских символов не содержать пробелов и быть более 8 символов')])


class UserChangeAccount(ModelForm):
    first_name = forms.CharField(max_length=20,
                                  validators=[RegexValidator(
                                    r"^[-a-zA-Z0-9_А-Яа-я]+\Z",
                                    "Name не должно быть не менее 3 и не более 20 символов и не содержать пробелов"),
                                      MaxLengthValidator(20),
                                      MinLengthValidator(3)])

    class Meta:
        model = User
        fields = ('first_name', )

