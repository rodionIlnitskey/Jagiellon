# Generated by Django 2.2 on 2021-03-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210320_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(default=None, max_length=20, verbose_name='имя'),
        ),
    ]
