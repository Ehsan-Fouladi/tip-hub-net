# Generated by Django 4.1.3 on 2022-11-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
