# Generated by Django 4.2.5 on 2023-09-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzmodels', '0004_remove_lessonview_viewedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Product', max_length=200),
        ),
    ]
