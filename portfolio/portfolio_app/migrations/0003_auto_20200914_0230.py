# Generated by Django 3.1.1 on 2020-09-13 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_remove_home_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tags',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='home',
            name='tags',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.tags'),
            preserve_default=False,
        ),
    ]