# Generated by Django 4.1.7 on 2023-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0012_alter_ngo_registration_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='registration_proof',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]