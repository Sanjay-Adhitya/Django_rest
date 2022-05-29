# Generated by Django 3.1 on 2022-05-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('Fund_id', models.AutoField(primary_key=True, serialize=False)),
                ('Fund_data', models.JSONField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Member_id', models.AutoField(primary_key=True, serialize=False)),
                ('Member_name', models.CharField(max_length=200)),
            ],
        ),
    ]
