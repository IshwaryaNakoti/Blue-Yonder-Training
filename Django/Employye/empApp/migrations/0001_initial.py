# Generated by Django 5.0.6 on 2024-06-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=30)),
                ('empNo', models.IntegerField()),
                ('empSal', models.FloatField()),
                ('empAddress', models.CharField(max_length=50)),
            ],
        ),
    ]
