# Generated by Django 4.1.3 on 2022-11-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_remove_video_title_video_body_alter_video_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='body',
            field=models.TextField(verbose_name='متن'),
        ),
    ]
