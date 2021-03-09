# Generated by Django 2.2.19 on 2021-03-08 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0124_auto_20210301_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateRoleAssignmentsWithCustomersConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('role', models.CharField(blank=True, choices=[('enterprise_admin', 'enterprise_admin'), ('enterprise_learner', 'enterprise_learner'), ('enterprise_catalog_admin', 'enterprise_catalog_admin'), ('enterprise_openedx_operator', 'enterprise_openedx_operator')], help_text='Specifies which user role assignments to update.  If unspecified, will update for all roles.', max_length=100)),
                ('batch_size', models.IntegerField(default=500, help_text='Number of user role asssignments to update in each batch of updates.')),
                ('enterprise_customer_uuid', models.CharField(blank=True, help_text='The enterprise customer to limit role assignments to.', max_length=36)),
                ('dry_run', models.BooleanField(default=True, help_text='If set, no updates or creates will occur; will instead iterate over the assignments that would be modified or created')),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
        ),
    ]