# Generated by Django 4.1 on 2022-10-25 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 25, 18, 50, 12, 463617, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 25, 18, 50, 12, 462617, tzinfo=datetime.timezone.utc)),
        ),
    ]
