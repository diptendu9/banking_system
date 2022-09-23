# Generated by Django 4.1.1 on 2022-09-21 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0009_accholder_email_accholder_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accholder',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=280234663, unique=True),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('transfer_date', models.DateTimeField(auto_now=True)),
                ('transact_date', models.DateTimeField(auto_now=True)),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='banking.accholder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='banking.accholder')),
            ],
        ),
    ]