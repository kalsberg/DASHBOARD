# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-01 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('icon', models.FileField(upload_to=b'categories')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=1000)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dashboard Links',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('icon', models.FileField(upload_to=b'sub_categories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Category')),
            ],
            options={
                'verbose_name_plural': 'Sub-categories',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.SubCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together=set([('name', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together=set([('name', 'sub_category')]),
        ),
    ]
