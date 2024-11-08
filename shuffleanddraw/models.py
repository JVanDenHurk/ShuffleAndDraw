from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price for customer

    def __str__(self):
        return self.name
