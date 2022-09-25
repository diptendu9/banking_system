# Generated by Django 4.1.1 on 2022-09-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0015_alter_accholder_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='aadhaar',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=341009557, unique=True),
        ),
        migrations.AlterField(
            model_name='accholder',
            name='pan',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]