# Generated by Django 3.1.1 on 2020-09-16 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=120)),
                ('quantity', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('datetime', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('finalOffer', models.IntegerField()),
                ('sendEmail', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.items')),
            ],
        ),
    ]
