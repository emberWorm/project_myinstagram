# Generated by Django 5.1.6 on 2025-03-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_userprofile_avatar_userprofile_bio_userprofile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
