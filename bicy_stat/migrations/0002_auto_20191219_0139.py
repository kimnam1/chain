# Generated by Django 2.2.6 on 2019-12-19 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bicy_stat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bicy_stats',
            options={'ordering': ('-period',), 'verbose_name': 'stat', 'verbose_name_plural': 'stats'},
        ),
    ]
