# Generated by Django 4.1.2 on 2022-11-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.IntegerField(verbose_name='bank_id'),
        ),
    ]