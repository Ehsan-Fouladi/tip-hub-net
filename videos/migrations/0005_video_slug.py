# Generated by Django 4.1.1 on 2022-11-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_rename_img_video_image_rename_name_video_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
