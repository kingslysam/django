# Generated by Django 4.1 on 2022-09-11 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0011_service_transaction_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_charge',
        ),
    ]
