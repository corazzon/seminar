# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 13:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meetup', '0002_auto_20170903_1001'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_canceled', models.BooleanField(default=False)),
                ('payment_method', models.CharField(choices=[('credit', 'Credit Card')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_canceled', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('charge', models.PositiveIntegerField(default=0)),
                ('maximum_count', models.PositiveIntegerField(default=0)),
                ('start_time_to_sell', models.DateTimeField(default=django.utils.timezone.now)),
                ('sold_out_by_admin', models.BooleanField(default=True)),
                ('meet_up', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meetup.MeetUp')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Ticket'),
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Registration'),
        ),
        migrations.AddField(
            model_name='attendcheck',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Registration'),
        ),
    ]
