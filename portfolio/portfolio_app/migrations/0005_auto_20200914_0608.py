# Generated by Django 3.1.1 on 2020-09-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_auto_20200914_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='email',
            field=models.EmailField(default='sunnydecent11@gmail.com', max_length=20),
        ),
        migrations.AddField(
            model_name='home',
            name='phone',
            field=models.IntegerField(default='8383966836', max_length=12),
        ),
    ]
