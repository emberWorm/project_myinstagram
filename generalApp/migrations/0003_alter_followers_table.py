# Generated by Django 5.1.6 on 2025-02-17 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalApp', '0002_alter_followers_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='followers',
            table='Followers',
        ),
    ]
