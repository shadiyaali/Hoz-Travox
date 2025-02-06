# Generated by Django 5.1.5 on 2025-02-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_service_alter_usermanagement_unique_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField(blank=True, null=True)),
                ('item_name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('payable_to', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
