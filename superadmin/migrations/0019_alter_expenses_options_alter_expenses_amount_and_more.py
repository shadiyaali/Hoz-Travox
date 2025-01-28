# Generated by Django 5.1.4 on 2024-12-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0018_expenses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'verbose_name_plural': 'Expenses'},
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('partially_paid', 'Partially Paid')], default='unpaid', max_length=20),
        ),
    ]
