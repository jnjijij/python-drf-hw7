# Generated by Django 5.0.1 on 2024-02-05 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'Only alphanumeric 2-20 characters allowed.')])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)])),
                ('year', models.IntegerField()),
                ('body_type', models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Jeep', 'Jeep')], max_length=9)),
            ],
            options={
                'db_table': 'cars',
                'ordering': ['-id'],
            },
        ),
    ]