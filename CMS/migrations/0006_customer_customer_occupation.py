# Generated by Django 4.1 on 2022-08-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0005_customer_customer_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_occupation',
            field=models.CharField(default='Not Enter', max_length=100),
        ),
    ]