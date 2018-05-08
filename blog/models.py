from django.db import models
from django.utils import timezone

class CommonInfo(models.Model):
    'Абстрактная модель для общих полей'
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.CharField(max_length=160, blank=True, null=True, verbose_name='Краткое описание')
    to_publish = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        abstract = True

class Rubric(CommonInfo):

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __str__(self):
        return self.title


class Post(CommonInfo):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, verbose_name="Рубрика")
    slug = models.CharField(max_length=200, unique=True, verbose_name='url статьи')    
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ключевые слова')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title