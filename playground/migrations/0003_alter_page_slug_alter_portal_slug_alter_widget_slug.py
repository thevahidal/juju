# Generated by Django 5.1 on 2024-08-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_portal_widget_page_pagewidget_page_widgets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='portal',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
