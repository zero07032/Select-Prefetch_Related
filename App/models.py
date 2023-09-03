from django.db import models


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk}.{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=250)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}.{self.name}"
