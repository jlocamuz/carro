# Generated by Django 3.2.7 on 2022-04-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro1', '0007_sale_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saledetail',
            name='product',
            field=models.CharField(max_length=50),
        ),
    ]
