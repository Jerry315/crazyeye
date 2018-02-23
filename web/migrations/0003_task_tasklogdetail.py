# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.SmallIntegerField(choices=[(0, 'cmd'), (1, 'file_transfer')])),
                ('content', models.TextField(verbose_name='任务内容')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(0, 'success'), (1, 'failed'), (2, 'init')])),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('bind_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHost')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Task')),
            ],
        ),
    ]
