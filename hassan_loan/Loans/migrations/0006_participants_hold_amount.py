# Generated by Django 3.0.2 on 2020-02-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0005_auto_20200207_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='hold_amount',
            field=models.IntegerField(default=0),
        ),
    ]
