# Generated by Django 2.2 on 2021-03-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_delete_likedislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='author_name',
            field=models.CharField(max_length=20, null=True, verbose_name='имя'),
        ),
    ]
