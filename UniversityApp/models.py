from django.db import models

# Create your models here.
class University(models.Model):
    title = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length=50)
    birthday = models.DateField()
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)
    receipt_year = models.IntegerField()

    def __str__(self):
        return self.name

