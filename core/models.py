from django.db import models


class MainMenu(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, verbose_name='Метка')
    usort = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=1)
    is_main = models.

class CoreData(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    to_publish = models.BooleanField(verbose_name='Опубликовать', default=True)
    on_main = models.BooleanField(verbose_name='На главной', default=False)
    usort = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=1)

    class Meta:
        verbose_name = 'Данные сайта'
        verbose_name_plural = 'Данные сайта'
    
    def __str__(self):
        return self.title

class Contacts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    country = models.CharField(max_length=100, verbose_name='Страна', blank=True)
    city = models.CharField(max_length=50, verbose_name='Город', blank=True)
    street = models.CharField(max_length=100, verbose_name='Улица', blank=True)
    home = models.CharField(max_length=10, verbose_name='Дом', blank=True)
    ofice = models.CharField(max_length=10, verbose_name='Офис', blank=True)
    phone_1 = models.CharField(max_length=20, verbose_name='Телефон 1', blank=True)
    phone_2 = models.CharField(max_length=20, verbose_name='Телефон 2', blank=True)
    mail = models.EmailField(max_length=254, verbose_name='email', blank=True)
    # soc = 

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title

class SocNet(models.Model):
    pass