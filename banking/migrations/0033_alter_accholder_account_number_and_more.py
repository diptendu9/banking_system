# Generated by Django 4.1.1 on 2022-09-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0032_transactions_reciver_alter_accholder_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=654943971, unique=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='reciver',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='t_type',
            field=models.CharField(choices=[('Deposited', 'Deposit'), ('Withdrawn', 'Withdraw')], max_length=9, null=True),
        ),
    ]
