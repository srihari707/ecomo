# Generated by Django 4.1.4 on 2023-03-01 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_caetitem_cartitem_alter_cart_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='Product',
        ),
    ]
