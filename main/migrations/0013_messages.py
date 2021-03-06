# Generated by Django 3.1.1 on 2020-09-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200920_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.CharField(max_length=256)),
                ('response', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
