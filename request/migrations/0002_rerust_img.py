# Generated by Django 4.1.7 on 2023-06-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rerust',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
