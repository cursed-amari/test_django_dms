import datetime

from django.conf import settings
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

def user_name(instance):
    return instance.user.username



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = datetime.datetime.now().strftime("%Y-%m-%d").split("-")
    return f"adventure/{now[0]}/{now[1]}/{now[2]}/user_{instance.user.username}/{filename}"


class Adventure(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    amount_players = models.IntegerField(verbose_name="Количество игроков",
                                         validators=[MaxValueValidator(20), MinValueValidator(1)])
    duration = models.IntegerField(verbose_name="Примерная длительность", null=True, blank=True,
                                   validators=[MaxValueValidator(20), MinValueValidator(1)])
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to=user_directory_path,
        null=True, blank=True,
        default="adventure/default/default_img_test.png")
    file = models.FileField(
        verbose_name="Файл",
        upload_to=user_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['rar', 'zip', 'json'])])
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Отредактирован")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, null=True, blank=True, default=6)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adventure', kwargs={'adventure_slug': self.slug})

    class Meta:
        verbose_name = 'Приключение'
        verbose_name_plural = 'Приключения'
        ordering = ['time_update']
