# Generated by Django 2.2.1 on 2019-07-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190713_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='hotel_Main_Img',
            new_name='uploaded_image',
        ),
    ]
