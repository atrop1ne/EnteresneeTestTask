from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='аватарка пользователя', null=True, blank=True, upload_to='photos/')

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        try:
            instance.account.save()
        except ObjectDoesNotExist:
            Account.objects.create(user=instance)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f"{self.user}"

    @property
    def places(self):
        return Place.objects.filter(account = self)

class Place(models.Model):
    name = models.CharField(verbose_name='наименование места', null=False, max_length=50)
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)
    lng = models.DecimalField(verbose_name='широта', max_digits=30, decimal_places=25, null=True, blank=True)
    lat = models.DecimalField(verbose_name='долгота', max_digits=30, decimal_places=25, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name