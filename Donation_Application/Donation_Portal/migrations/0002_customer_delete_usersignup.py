# Generated by Django 4.1.7 on 2023-09-29 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donation_Portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Andra Pradesh', 'Andra Pradesh'), ('Punjab', 'Punjab'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Karnataka', 'Karnataka'), ('Gujrat', 'Gujrat'), ('Rajasthan', 'Rajasthan'), ('Assam', 'Assam'), ('Chandigarh', 'Chandigarh'), ('Maharashtra', 'Maharashtra')], max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='userSignup',
        ),
    ]