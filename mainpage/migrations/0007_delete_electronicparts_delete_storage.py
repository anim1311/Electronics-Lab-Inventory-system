# Generated by Django 4.1.6 on 2023-02-13 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_datasheet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Electronicparts',
        ),
        migrations.DeleteModel(
            name='STORAGE',
        ),
    ]