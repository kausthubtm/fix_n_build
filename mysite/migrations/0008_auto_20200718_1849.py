# Generated by Django 3.0.7 on 2020-07-18 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_applications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applications',
            new_name='Application',
        ),
    ]