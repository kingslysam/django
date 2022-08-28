# Generated by Django 4.1 on 2022-08-25 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0003_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField(unique=True)),
                ('staff_name', models.CharField(max_length=255)),
                ('staff_position', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StaffCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.customer')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.staff')),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_of_kin_name', models.CharField(max_length=255, unique=True)),
                ('next_of_kin_contact', models.CharField(max_length=15)),
                ('next_of_kin_residence', models.CharField(max_length=25)),
                ('next_of_kin_nida', models.IntegerField(unique=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.account')),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.customer')),
            ],
        ),
    ]