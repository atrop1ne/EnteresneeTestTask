# Generated by Django 3.2 on 2021-05-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlaceRememberApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ссылка на аватар'),
        ),
    ]