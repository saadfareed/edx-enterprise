# Generated by Django 3.2.23 on 2024-01-10 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0030_integratedchannelapirequestlogs'),
        ('cornerstone', '0030_auto_20231010_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='CornerstoneAPIRequestLogs',
            fields=[
                ('integratedchannelapirequestlogs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrated_channel.integratedchannelapirequestlogs')),
                ('user_agent', models.CharField(max_length=255)),
                ('user_ip', models.GenericIPAddressField()),
            ],
            bases=('integrated_channel.integratedchannelapirequestlogs',),
        ),
    ]
