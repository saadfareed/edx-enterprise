# Generated by Django 3.2.12 on 2022-07-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0161_alter_enterprisecustomerreportingconfiguration_data_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_executive_education_2U_fulfillment',
            field=models.BooleanField(default=False, help_text='Specifies whether the enterprise should have access to Executive Education (2U) content.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_executive_education_2U_fulfillment',
            field=models.BooleanField(default=False, help_text='Specifies whether the enterprise should have access to Executive Education (2U) content.'),
        ),
    ]
