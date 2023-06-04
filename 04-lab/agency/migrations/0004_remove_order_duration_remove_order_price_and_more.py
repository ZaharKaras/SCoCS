# Generated by Django 4.2.1 on 2023-06-04 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_delete_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='departure_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='package',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
