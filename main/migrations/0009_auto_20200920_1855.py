# Generated by Django 3.1.1 on 2020-09-20 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_item_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='cena',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='ime',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='stock',
            new_name='lager',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='opis',
        ),
    ]
