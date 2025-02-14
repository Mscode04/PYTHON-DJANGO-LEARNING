# Generated by Django 5.1.4 on 2025-01-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weather', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('google_map_link', models.URLField(max_length=500)),
                ('place_image', models.ImageField(upload_to='places/')),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
    ]
