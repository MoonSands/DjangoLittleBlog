# Generated by Django 5.0 on 2024-05-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_feed', '0011_docs_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
