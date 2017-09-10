# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 14:36
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='The email was used to sign in')),
                ('token',
                 models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='The token was generated by uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='username')),
                ('organization', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='profile')),
                ('biography', models.TextField(max_length=4000, null=True)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brief', models.TextField(null=True, verbose_name='simple information')),
                ('description', models.TextField(null=True)),
                ('slide_url', models.URLField(null=True, verbose_name='A slide url')),
                ('pdf_url', models.URLField(null=True, verbose_name='A pdf url')),
                ('video_url', models.URLField(null=True, verbose_name='A video url')),
                ('is_recordable', models.BooleanField(default=True, verbose_name='recordable condition')),
                ('is_main_event', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetup.ProgramCategory',
                                    verbose_name='The category which this program is belonged'),
        ),
        migrations.AddField(
            model_name='program',
            name='speakers',
            field=models.ManyToManyField(null=True, to='meetup.Speaker'),
        ),
    ]