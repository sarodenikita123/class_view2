# Generated by Django 5.0.4 on 2024-04-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_last_name', models.CharField(max_length=20)),
                ('customer_account_no', models.CharField(max_length=20)),
                ('bank_branch', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]