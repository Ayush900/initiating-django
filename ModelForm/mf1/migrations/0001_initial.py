# Generated by Django 2.2a1 on 2019-08-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email_id', models.EmailField(max_length=254)),
                ('branch', models.CharField(max_length=300)),
                ('Date_of_birth', models.DateField()),
                ('phone_no', models.IntegerField(unique=True)),
            ],
        ),
    ]
