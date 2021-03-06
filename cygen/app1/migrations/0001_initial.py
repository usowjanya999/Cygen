# Generated by Django 3.0.5 on 2020-08-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('empno', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='cygen_images/')),
                ('Startdate', models.DateField()),
                ('Customers', models.IntegerField()),
            ],
        ),
    ]
