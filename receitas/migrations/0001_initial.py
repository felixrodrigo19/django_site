# Generated by Django 4.0.5 on 2022-06-11 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 6, 11, 9, 32, 34, 379685))),
            ],
        ),
    ]
