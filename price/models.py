from django.db import models


# Create your models here.
class PriceCard(models.Model):
    price_card_value = models.CharField(max_length=20, verbose_name='Цена')
    price_card_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.price_card_value

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    price_table_title = models.CharField(max_length=200, verbose_name='Услуга')
    price_table_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    price_table_new_price = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.price_table_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'