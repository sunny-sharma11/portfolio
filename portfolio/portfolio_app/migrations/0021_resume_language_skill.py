# Generated by Django 3.1.1 on 2020-09-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0020_resume_education_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_language_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('skill_rating', models.ImageField(upload_to='')),
            ],
        ),
    ]