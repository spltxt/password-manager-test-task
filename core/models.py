from django.db import models

class Account(models.Model):
    website = models.CharField(max_length=50, verbose_name="Сайт")
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Электронная почта")
    password = models.CharField(max_length=30, verbose_name="Пароль")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website

    class Meta:
        ordering = ('created',)



