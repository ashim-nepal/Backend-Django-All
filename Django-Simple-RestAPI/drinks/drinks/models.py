from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=175)
    description = models.CharField(max_length=625)
    
    # To make the database name distinct based on name in admin db
    def __str__(self):
        return self.name