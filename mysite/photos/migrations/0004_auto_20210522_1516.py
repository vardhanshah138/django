# Generated by Django 2.2.22 on 2021-05-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20210522_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='record_img',
            new_name='image_upload',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='record_vid',
            new_name='video_upload',
        ),
    ]
