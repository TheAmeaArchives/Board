# Generated by Django 5.1.4 on 2025-01-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leader', '0004_remove_curation_points_post_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='curation',
            name='sub_title',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curation',
            name='title',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
    ]