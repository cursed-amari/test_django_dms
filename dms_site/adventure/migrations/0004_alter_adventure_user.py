# Generated by Django 4.1.7 on 2023-03-09 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adventure', '0003_alter_adventure_slug_alter_adventure_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventure',
            name='user',
            field=models.ForeignKey(blank=True, default=6, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
