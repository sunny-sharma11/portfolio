# Generated by Django 3.1.1 on 2020-09-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_auto_20200914_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='email',
            field=models.EmailField(default='sunnydecent11@gmail.com', max_length=50),
        ),
    ]
