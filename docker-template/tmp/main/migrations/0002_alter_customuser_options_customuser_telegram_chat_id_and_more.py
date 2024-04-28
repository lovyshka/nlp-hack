# Generated by Django 4.1.1 on 2023-07-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram_chat_id',
            field=models.PositiveBigIntegerField(null=True, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='verified_usr',
            field=models.BooleanField(default=False, verbose_name='Верификация пользователя'),
        ),
    ]