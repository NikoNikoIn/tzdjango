# Generated by Django 4.2.5 on 2023-09-26 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0013_alter_lessonview_lastview_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonview',
            name='lastView',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 11, 0, 58, 446153, tzinfo=datetime.timezone.utc)),
        ),
    ]
