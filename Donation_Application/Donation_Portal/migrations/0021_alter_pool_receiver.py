# Generated by Django 4.1.7 on 2023-10-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0020_alter_transaction_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='receiver',
            field=models.CharField(max_length=30),
        ),
    ]