# Generated by Django 4.1.7 on 2023-06-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_remove_rerust_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='rerust',
            name='question2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
