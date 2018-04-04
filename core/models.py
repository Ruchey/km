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