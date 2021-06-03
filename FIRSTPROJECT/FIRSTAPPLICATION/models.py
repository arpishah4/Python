from django.db import models
#from django.db.models.fields import CharField


class Persons(models.Model):
    name=models.CharField(max_length=15)
    contact=models.IntegerField()
    address=models.TextField(blank=True)
    age=models.IntegerField()

    def __str__(self):
        return self.name