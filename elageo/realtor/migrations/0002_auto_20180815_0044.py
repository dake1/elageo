# Generated by Django 2.1 on 2018-08-15 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='property',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='image',
        ),
    ]
