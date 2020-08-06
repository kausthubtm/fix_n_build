from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=10)
    type = models.CharField(max_length=40)
    wage = models.CharField(max_length=5)
    experience = models.CharField(max_length=5)
    review = models.CharField(max_length=10, default='null')


class Application(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    job_type = models.CharField(max_length=20)
    job_experience = models.CharField(max_length=5)
