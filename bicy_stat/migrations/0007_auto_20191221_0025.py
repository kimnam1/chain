# Generated by Django 2.2.6 on 2019-12-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicy_stat', '0006_auto_20191220_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='stationId',
            field=models.CharField(max_length=50, unique=True, verbose_name='ID'),
        ),
    ]
