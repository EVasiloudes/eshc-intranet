# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_current_member_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='extra_ldap_groups',
            field=models.ManyToManyField(blank=True, to='home.LdapGroup'),
        ),
    ]
