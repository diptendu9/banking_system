# Generated by Django 4.1.1 on 2022-09-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0010_accholder_date_alter_accholder_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=996336716, unique=True),
        ),
    ]
