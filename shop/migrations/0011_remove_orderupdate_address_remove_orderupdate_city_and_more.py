# Generated by Django 4.2.1 on 2023-07-07 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderupdate',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orderupdate',
            name='phoneNo',
        ),
        migrations.RemoveField(
            model_name='orderupdate',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orderupdate',
            name='zip_code',
        ),
    ]
