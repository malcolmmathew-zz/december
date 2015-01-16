# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=25)),
                ('task_description', models.CharField(max_length=250)),
                ('deadline_date', models.DateTimeField(verbose_name=b'Deadline Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
