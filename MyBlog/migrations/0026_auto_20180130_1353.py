# Generated by Django 2.0.1 on 2018-01-30 13:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0025_comment2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_txt',
            field=tinymce.models.HTMLField(default='hllo', max_length=100),
        ),
    ]