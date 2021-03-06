# Generated by Django 2.1.7 on 2019-03-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190309_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='art/'),
        ),
        migrations.AddField(
            model_name='art',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='art/'),
        ),
        migrations.AddField(
            model_name='art',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='art/'),
        ),
        migrations.AlterField(
            model_name='art',
            name='best_size',
            field=models.CharField(blank=True, choices=[('5x5', '5x5'), ('10x10', '10x10')], max_length=15),
        ),
        migrations.AlterField(
            model_name='commission',
            name='size',
            field=models.CharField(choices=[('5x5', '5x5'), ('10x10', '10x10')], max_length=15),
        ),
    ]
