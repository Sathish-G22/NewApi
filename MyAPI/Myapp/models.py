from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.name