# Generated by Django 2.0.3 on 2018-04-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('home', models.CharField(max_length=10, verbose_name='Дом')),
                ('office', models.CharField(max_length=10, verbose_name='Офис')),
                ('phone_1', models.CharField(max_length=20, verbose_name='Телефон 1')),
                ('phone_2', models.CharField(max_length=20, verbose_name='Телефон 2')),
                ('mail', models.CharField(max_length=20, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='SocNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='coredata',
            old_name='html_text',
            new_name='text',
        ),
    ]