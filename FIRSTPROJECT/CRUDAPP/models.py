from django.db import models
 #so created the model
class books(models.Model):
    name=models.CharField(max_length=25)
    pages=models.IntegerField()

    def __str__(self):
        return self.name
