# Generated by Django 4.2.5 on 2023-09-25 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0010_lessonview_lastview'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonview',
            name='inProduct',
            field=models.ManyToManyField(to='tzmodels.product'),
        ),
        migrations.AlterField(
            model_name='lessonview',
            name='lastView',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 25, 21, 53, 7, 998738, tzinfo=datetime.timezone.utc)),
        ),
    ]
