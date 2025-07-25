# Generated by Django 5.0.1 on 2025-02-03 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event', models.CharField(max_length=500)),
                ('Dis', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('rid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userrequest')),
            ],
        ),
    ]
