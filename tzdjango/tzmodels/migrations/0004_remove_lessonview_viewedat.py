# Generated by Django 4.2.5 on 2023-09-25 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0003_lessonview_viewedtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonview',
            name='viewedAt',
        ),
    ]
