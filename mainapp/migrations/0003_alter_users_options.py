# Generated by Django 3.2.8 on 2021-10-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211012_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['surname']},
        ),
    ]