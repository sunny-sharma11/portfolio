# Generated by Django 3.1.1 on 2020-09-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0025_resume_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]