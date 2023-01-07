from django.db import models


# Create your models here.
class TeleSettings(models.Model):
    telegram_token = models.CharField(max_length=200, verbose_name='Телеграм токен')
    telegram_chat_id = models.CharField(max_length=200, verbose_name='Айди чата')
    telegram_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.telegram_chat_id

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'