# Generated by Django 2.1.1 on 2018-09-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ensUserId', models.CharField(max_length=255, verbose_name='エンドユーザID')),
                ('userId', models.CharField(max_length=255, verbose_name='ユーザID')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
            ],
        ),
    ]