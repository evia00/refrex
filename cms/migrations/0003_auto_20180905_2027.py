# Generated by Django 2.1.1 on 2018-09-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='accesstoken',
            name='regTs',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='regTs',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='regTs',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='ユーザID'),
        ),
    ]
