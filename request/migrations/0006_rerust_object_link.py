# Generated by Django 4.1.7 on 2023-07-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_rerust_id_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='rerust',
            name='object_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]