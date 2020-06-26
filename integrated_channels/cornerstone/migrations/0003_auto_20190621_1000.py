# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 10:00


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0002_cornerstoneglobalconfiguration_subject_mapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='cornerstoneglobalconfiguration',
            name='key',
            field=models.CharField(default='key', help_text='Basic auth username for sending user completion status to cornerstone.', max_length=255, verbose_name='Basic Auth username'),
        ),
        migrations.AddField(
            model_name='cornerstoneglobalconfiguration',
            name='secret',
            field=models.CharField(default='secret', help_text='Basic auth password for sending user completion status to cornerstone.', max_length=255, verbose_name='Basic Auth password'),
        ),
        migrations.AddField(
            model_name='cornerstonelearnerdatatransmissionaudit',
            name='grade',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornerstonelearnerdatatransmissionaudit',
            name='enterprise_course_enrollment_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
