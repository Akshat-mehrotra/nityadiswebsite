# Generated by Django 2.1.7 on 2019-03-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190309_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='cropping',
        ),
        migrations.AddField(
            model_name='art',
            name='cropped',
            field=models.ImageField(blank=True, null=True, upload_to='art_croped/'),
        ),
    ]
