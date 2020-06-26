# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 20:27


import fernet_fields.fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0037_auto_20180110_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomerreportingconfiguration',
            name='decrypted_password',
            field=fernet_fields.fields.EncryptedCharField(blank=True, help_text='This password will be used to secure the zip file. It will be encrypted when stored in the database.', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='enterprisecustomerreportingconfiguration',
            name='decrypted_sftp_password',
            field=fernet_fields.fields.EncryptedCharField(blank=True, help_text='If the delivery method is sftp, the password to use to securely access the host. The password will be encrypted when stored in the database.', max_length=256, null=True),
        ),
    ]
