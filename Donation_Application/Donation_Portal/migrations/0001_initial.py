# Generated by Django 4.1.7 on 2023-09-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]
