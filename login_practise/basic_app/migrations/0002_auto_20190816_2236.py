# Generated by Django 2.2a1 on 2019-08-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamprofile',
            old_name='team_name',
            new_name='username',
        ),
    ]
