# Generated by Django 5.1.6 on 2025-02-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_beat_play_count_beat_sales_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_beats',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='store.beat'),
        ),
    ]
