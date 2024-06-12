# Generated by Django 5.0 on 2024-06-12 14:00

import django_editorjs_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('blog', 'blog'), ('projects', 'projects')], default='blog', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_editorjs_fields.fields.EditorJsJSONField(),
        ),
        migrations.AlterField(
            model_name='postcontentfilesupload',
            name='file',
            field=models.FileField(upload_to='media/uploads'),
        ),
        migrations.DeleteModel(
            name='postCategory',
        ),
    ]