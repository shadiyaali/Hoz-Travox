# Generated by Django 5.1.4 on 2024-12-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0016_paymentreceived_invoice_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('opening_balance', models.IntegerField(default=0)),
            ],
        ),
    ]
