from django.db import models

class Tovar(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=10)
    def __str__(self):
        return self.name