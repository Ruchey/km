from django.db import models

class CoreData(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    html_text = models.TextField(verbose_name='Текст')
    to_publish = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        verbose_name = 'Данные сайта'
        verbose_name_plural = 'Данные сайта'
    
    def __str__(self):
        return self.title

class Contacts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    home = models.CharField(max_length=10, verbose_name='Дом')
    office = models.CharField(max_length=10, verbose_name='Офис')
    phone_1 = models.CharField(max_length=20, verbose_name='Телефон 1')
    phone_2 = models.CharField(max_length=20, verbose_name='Телефон 2')
    mail = models.CharField(max_length=20, verbose_name='email')
    # soc = 

class SocNet(models.Model):
    pass