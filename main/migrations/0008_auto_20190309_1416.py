# Generated by Django 2.1.7 on 2019-03-09 14:16

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_art_croppin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='croppin',
        ),
        migrations.AddField(
            model_name='art',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('picture', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]