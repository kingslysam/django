# Generated by Django 4.1 on 2022-08-25 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0002_account_alter_customer_customer_birth_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField()),
                ('loan_type', models.CharField(max_length=20)),
                ('loan_start_date', models.DateField()),
                ('loan_duration', models.IntegerField()),
                ('loan_interest_rate', models.IntegerField()),
                ('loan_amount_paid', models.FloatField()),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.customer')),
            ],
        ),
    ]
