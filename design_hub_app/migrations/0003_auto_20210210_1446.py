# Generated by Django 3.1.6 on 2021-02-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design_hub_app', '0002_auto_20210205_2250'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visitor',
            new_name='Guest',
        ),
    ]
