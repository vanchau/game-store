# Generated by Django 3.0.2 on 2020-02-02 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0014_remove_purchase_checksum'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_complete',
            field=models.BooleanField(default=False),
        ),
    ]
