# Generated by Django 5.0.2 on 2024-02-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл.почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
