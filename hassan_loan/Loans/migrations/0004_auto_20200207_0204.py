# Generated by Django 3.0.2 on 2020-02-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0003_auto_20200205_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='totla_loan_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='pyment_remaining',
        ),
    ]
