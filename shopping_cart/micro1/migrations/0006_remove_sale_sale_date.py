# Generated by Django 3.2.7 on 2022-04-18 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micro1', '0005_alter_sale_sale_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='sale_date',
        ),
    ]
