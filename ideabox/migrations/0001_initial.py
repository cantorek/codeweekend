# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=2000)),
                ('author', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('date_added', models.DateTimeField(verbose_name='date added')),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard'), (4, 'Ultra')])),
                ('author', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(to='ideabox.Idea'),
        ),
    ]
