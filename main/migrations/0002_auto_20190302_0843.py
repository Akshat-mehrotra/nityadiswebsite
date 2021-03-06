# Generated by Django 2.1 on 2019-03-02 08:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='size1',
        ),
        migrations.RemoveField(
            model_name='art',
            name='size2',
        ),
        migrations.RemoveField(
            model_name='art',
            name='size3',
        ),
        migrations.RemoveField(
            model_name='art',
            name='size4',
        ),
        migrations.AddField(
            model_name='art',
            name='best_size',
            field=models.CharField(blank=True, choices=[('5"x5"', '5x5'), ('10"x10"', '10x10')], max_length=15),
        ),
        migrations.AddField(
            model_name='commission',
            name='address',
            field=models.CharField(default='asdfa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='email',
            field=models.EmailField(default='asdfdhh', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
