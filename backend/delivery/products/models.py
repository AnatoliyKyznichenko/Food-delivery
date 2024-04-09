from django.db import models

# Create your models here.
class Product_MY(models.Model):
    name=models.Model(models.CharField(max_length=150))
    def __str__(self):
        return self.name