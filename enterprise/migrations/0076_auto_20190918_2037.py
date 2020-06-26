# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-18 20:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0075_auto_20190916_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_portal_reporting_config_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the reporting configurations screen in the admin portal.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_portal_reporting_config_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the reporting configurations screen in the admin portal.'),
        ),
        migrations.AlterField(
            model_name='enterprisecustomer',
            name='learner_portal_hostname',
            field=models.CharField(blank=True, default='', help_text='Hostname of the enterprise learner portal, e.g. bestrun.edx.org.', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalenterprisecustomer',
            name='learner_portal_hostname',
            field=models.CharField(blank=True, default='', help_text='Hostname of the enterprise learner portal, e.g. bestrun.edx.org.', max_length=255),
        ),
    ]
