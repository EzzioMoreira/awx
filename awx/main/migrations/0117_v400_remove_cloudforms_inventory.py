# Generated by Django 2.2.11 on 2020-05-01 13:25

from django.db import migrations, models
from awx.main.migrations._inventory_source import create_scm_script_substitute


def convert_cloudforms_to_scm(apps, schema_editor):
    create_scm_script_substitute(apps, 'cloudforms')


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0116_v400_remove_hipchat_notifications'),
    ]

    operations = [
        migrations.RunPython(convert_cloudforms_to_scm),
        migrations.AlterField(
            model_name='inventorysource',
            name='source',
            field=models.CharField(choices=[('file', 'File, Directory or Script'), ('scm', 'Sourced from a Project'), ('ec2', 'Amazon EC2'), ('gce', 'Google Compute Engine'), ('azure_rm', 'Microsoft Azure Resource Manager'), ('vmware', 'VMware vCenter'), ('satellite6', 'Red Hat Satellite 6'), ('openstack', 'OpenStack'), ('rhv', 'Red Hat Virtualization'), ('tower', 'Ansible Tower'), ('custom', 'Custom Script')], default=None, max_length=32),
        ),
        migrations.AlterField(
            model_name='inventoryupdate',
            name='source',
            field=models.CharField(choices=[('file', 'File, Directory or Script'), ('scm', 'Sourced from a Project'), ('ec2', 'Amazon EC2'), ('gce', 'Google Compute Engine'), ('azure_rm', 'Microsoft Azure Resource Manager'), ('vmware', 'VMware vCenter'), ('satellite6', 'Red Hat Satellite 6'), ('openstack', 'OpenStack'), ('rhv', 'Red Hat Virtualization'), ('tower', 'Ansible Tower'), ('custom', 'Custom Script')], default=None, max_length=32),
        ),
    ]
