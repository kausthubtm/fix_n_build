# Generated by Django 3.0.7 on 2020-07-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_worker_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=60)),
                ('phone_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('job_type', models.CharField(max_length=20)),
                ('job_experience', models.CharField(max_length=5)),
            ],
        ),
    ]