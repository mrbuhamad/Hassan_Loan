# Generated by Django 3.0.2 on 2020-01-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyments',
            name='date',
            field=models.DateField(),
        ),
    ]