# Generated by Django 4.1.6 on 2023-02-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='STORAGE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=200)),
                ('longname', models.CharField(max_length=200)),
                ('shortname', models.CharField(max_length=200)),
                ('responsible_person', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('title_de', models.CharField(max_length=200)),
            ],
        ),
    ]