# Generated by Django 3.2.7 on 2022-04-18 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro1', '0003_alter_cartdetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]