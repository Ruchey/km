# Generated by Django 2.0.3 on 2018-04-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180405_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='coredata',
            name='usort',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Сортировка'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='coredata',
            name='on_main',
            field=models.BooleanField(default=False, verbose_name='На главной'),
        ),
    ]
