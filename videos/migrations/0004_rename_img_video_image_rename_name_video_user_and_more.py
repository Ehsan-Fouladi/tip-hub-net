# Generated by Django 4.1.1 on 2022-11-15 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_img_video_name_video_slug_alter_video_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
    ]
