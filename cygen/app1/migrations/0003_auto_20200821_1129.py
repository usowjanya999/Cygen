# Generated by Django 3.0.5 on 2020-08-21 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200821_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Image',
            new_name='photo',
        ),
    ]