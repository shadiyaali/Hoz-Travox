# Generated by Django 5.1.4 on 2024-12-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True, verbose_name='Account Number')),
                ('account_holder_name', models.CharField(max_length=100, verbose_name='Account Holder Name')),
                ('bank_name', models.CharField(max_length=100, verbose_name='Bank Name')),
                ('branch_name', models.CharField(max_length=100, verbose_name='Branch Name')),
                ('ifsc_code', models.CharField(max_length=11, verbose_name='IFSC Code')),
            ],
        ),
    ]
