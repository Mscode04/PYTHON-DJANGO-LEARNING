# Generated by Django 5.1.4 on 2025-01-05 19:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_recipes_vegetarian'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='Recipe_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='recipe/'),
            preserve_default=False,
        ),
    ]
