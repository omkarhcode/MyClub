# Generated by Django 3.2.2 on 2021-05-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210512_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='Contact Phone'),
        ),
    ]
