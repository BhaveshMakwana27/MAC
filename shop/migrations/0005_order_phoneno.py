# Generated by Django 4.2.1 on 2023-07-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phoneNo',
            field=models.CharField(default='', max_length=100),
        ),
    ]