# Generated by Django 5.0.1 on 2024-01-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0002_remove_invoice_total_invoice_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number_of_hours',
            field=models.PositiveIntegerField(),
        ),
    ]
