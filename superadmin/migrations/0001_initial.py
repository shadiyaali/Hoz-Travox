# Generated by Django 5.1.4 on 2024-12-23 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20)),
                ('staff_role', models.CharField(choices=[('Sales Staff', 'Sales Staff'), ('Accountant', 'Accountant')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100, unique=True)),
                ('duration', models.PositiveIntegerField(help_text='Duration in months')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True, unique=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_name_arabic', models.CharField(blank=True, max_length=255, null=True)),
                ('company_location', models.CharField(max_length=255)),
                ('number_of_branches', models.IntegerField()),
                ('contact_numbers', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254)),
                ('admin_email', models.EmailField(max_length=254)),
                ('contact_person_name', models.CharField(max_length=255)),
                ('company_address', models.TextField()),
                ('gst_or_vat_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe Later', 'Maybe Later')], max_length=20)),
                ('gst_or_vat_number', models.CharField(blank=True, max_length=255, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20)),
                ('default_services', models.CharField(choices=[('Air Ticketing', 'Air Ticketing'), ('Visa Services', 'Visa Services'), ('Insurance', 'Insurance'), ('Emigration', 'Emigration'), ('Attestation', 'Attestation'), ('Holiday Packages', 'Holiday Packages'), ('Hotel Booking', 'Hotel Booking'), ('Train Tickets', 'Train Tickets'), ('Other', 'Other')], max_length=255)),
                ('other_service_details', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_details', models.TextField()),
                ('bank_qr_code', models.ImageField(blank=True, null=True, upload_to='bank_qr_codes/')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('accounts_auditing_needed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe in future', 'Maybe in future')], max_length=20)),
                ('invoice_excel_upload_option', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='superadmin.subscription')),
            ],
        ),
    ]
