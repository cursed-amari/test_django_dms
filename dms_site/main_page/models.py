from django.db import models


class HomePost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create']
