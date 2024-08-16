# Generated by Django 5.1 on 2024-08-16 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('metadata_schema', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('add_to_menu', models.BooleanField(default=False)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.page')),
                ('portal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.portal')),
            ],
        ),
        migrations.CreateModel(
            name='PageWidget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.page')),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.widget')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='widgets',
            field=models.ManyToManyField(related_name='pages', through='playground.PageWidget', to='playground.widget'),
        ),
    ]