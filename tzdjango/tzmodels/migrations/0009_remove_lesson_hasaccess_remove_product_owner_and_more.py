# Generated by Django 4.2.5 on 2023-09-25 21:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tzmodels', '0008_lesson_hasaccess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='hasAccess',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
