# Generated by Django 3.0.2 on 2020-02-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0011_auto_20200202_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='pid',
        ),
        migrations.AddField(
            model_name='purchase',
            name='id',
            field=models.AutoField(auto_created=True, default=9999, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
