# Generated by Django 4.1.7 on 2023-06-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]