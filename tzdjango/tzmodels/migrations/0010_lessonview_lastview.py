# Generated by Django 4.2.5 on 2023-09-25 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0009_remove_lesson_hasaccess_remove_product_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonview',
            name='lastView',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 25, 21, 24, 55, 242047, tzinfo=datetime.timezone.utc)),
        ),
    ]
