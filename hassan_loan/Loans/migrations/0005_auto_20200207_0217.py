# Generated by Django 3.0.2 on 2020-02-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0004_auto_20200207_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='paid_amount',
            field=models.IntegerField(default=0),
        ),
    ]
