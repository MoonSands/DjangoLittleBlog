# Generated by Django 5.0 on 2024-06-08 12:04

import django_editorjs_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_editorjs_fields.fields.EditorJsJSONField(),
        ),
    ]