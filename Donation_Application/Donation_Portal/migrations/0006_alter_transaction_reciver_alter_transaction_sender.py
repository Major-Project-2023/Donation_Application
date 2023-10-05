# Generated by Django 4.1.7 on 2023-10-02 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donation_Portal', '0005_miner_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
