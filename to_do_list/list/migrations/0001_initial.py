# Generated by Django 5.1.1 on 2024-11-07 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('Date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=200)),
                ('Note', models.CharField(max_length=50)),
                ('Date_created', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.date')),
            ],
        ),
    ]