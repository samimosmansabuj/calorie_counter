# Generated by Django 5.0 on 2024-01-18 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie_Counter_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=9)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_calorie', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Date_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('need_calorie', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('today_total_calorie', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Iteam_Calorie_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('calorie', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_date', to='calorie_counter_app.date_model')),
            ],
        ),
    ]
