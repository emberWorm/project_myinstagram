# Generated by Django 5.1.6 on 2025-03-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalApp', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, default='', max_length=1024, null=True),
        ),
    ]
