# Generated by Django 4.2.1 on 2023-06-03 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_remove_client_email_client_address_client_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]