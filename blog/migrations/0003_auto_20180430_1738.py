# Generated by Django 2.0.3 on 2018-04-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default='gard', unique=True, verbose_name='url статьи'),
            preserve_default=False,
        ),
    ]
