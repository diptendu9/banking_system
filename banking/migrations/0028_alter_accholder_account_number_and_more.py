# Generated by Django 4.1.1 on 2022-09-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0027_alter_accholder_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=574326186, unique=True),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='reciver',
            field=models.CharField(max_length=50),
        ),
    ]
