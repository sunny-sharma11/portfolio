# Generated by Django 3.1.1 on 2020-09-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_auto_20200914_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
