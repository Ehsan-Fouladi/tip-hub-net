# Generated by Django 4.1.3 on 2022-11-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_alter_video_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(null=True, verbose_name='بازدید'),
        ),
    ]
