# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-20 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20190220_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.IntegerField(choices=[(-1, '删除'), (0, '禁用'), (1, '正常')], default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(-1, '删除'), (0, '禁用'), (1, '正常')], default=1),
        ),
    ]