from datetime import datetime

from django.db import models


# Create your models here.


class University(models.Model):
    title = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.now, blank=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)
    receipt_year = models.IntegerField(default=2015)

    def __str__(self):
        return self.full_name
