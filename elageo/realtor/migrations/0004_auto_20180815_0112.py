# Generated by Django 2.1 on 2018-08-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0003_auto_20180815_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='description',
            new_name='img_desc',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d'),
        ),
    ]