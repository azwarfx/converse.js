# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0064_auto_20160428_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='vcs',
            field=models.CharField(choices=[('git', 'Git'), ('gerrit', 'Gerrit'), ('subversion', 'Subversion'), ('mercurial', 'Mercurial')], default='git', help_text='Version control system to use to access your repository with translations.', max_length=20, verbose_name='Version control system'),
        ),
    ]