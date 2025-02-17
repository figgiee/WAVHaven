# Generated by Django 5.1.6 on 2025-02-17 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='store.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvoted_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
