# Generated by Django 5.1.1 on 2024-10-18 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_remove_product_image_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
