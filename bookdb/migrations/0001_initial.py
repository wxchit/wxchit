# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=200)),
                ('AuthorID', models.CharField(max_length=10)),
                ('Publisher', models.CharField(max_length=30)),
                ('PublishDate', models.DateField()),
                ('Price', models.FloatField()),
            ],
        ),
    ]
