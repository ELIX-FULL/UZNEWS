# Generated by Django 4.0.4 on 2023-10-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productmodel_product_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]