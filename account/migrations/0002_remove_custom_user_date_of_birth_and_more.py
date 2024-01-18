# Generated by Django 5.0 on 2024-01-18 17:38

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator]),
        ),
    ]
