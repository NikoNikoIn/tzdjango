# Generated by Django 4.2.5 on 2023-09-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0002_lesson_inproduct_lessonview'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonview',
            name='viewedTime',
            field=models.IntegerField(default=0),
        ),
    ]
