# Generated by Django 3.1.1 on 2020-09-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0016_auto_20200914_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('institute', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=50)),
                ('score', models.ImageField(upload_to='')),
            ],
        ),
    ]