# Generated by Django 4.1.7 on 2023-10-31 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0031_remove_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='type_user', to='Donation_Portal.usertype', to_field='user_type'),
            preserve_default=False,
        ),
    ]