# Generated by Django 3.0.2 on 2020-02-07 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0008_auto_20200208_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hold_amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_hold_amount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Loans.Participants')),
            ],
        ),
    ]
