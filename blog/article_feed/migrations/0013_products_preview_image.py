# Generated by Django 5.0 on 2024-05-18 20:29

import article_feed.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_feed', '0012_alter_docs_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='preview_image',
            field=models.ImageField(default='posts/moon.jpg', upload_to=article_feed.models.upload_to),
        ),
    ]
