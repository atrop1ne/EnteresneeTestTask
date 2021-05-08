from django.db import models
from django.conf import settings

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='аватарка пользователя', null=True, blank=True)

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
    address = models.CharField(verbose_name='адрес', null=False, max_length=60)
    location = models.CharField(verbose_name='координаты', null=False, max_length=60)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name