# Generated by Django 3.1.1 on 2020-09-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200920_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='quantity',
            new_name='quantity1',
        ),
        migrations.AddField(
            model_name='offer',
            name='quantity2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='quantity3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='quantity4',
            field=models.IntegerField(null=True),
        ),
    ]
