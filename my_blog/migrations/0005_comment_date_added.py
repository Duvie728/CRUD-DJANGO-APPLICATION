# Generated by Django 3.2 on 2021-05-05 01:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_auto_20210504_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
