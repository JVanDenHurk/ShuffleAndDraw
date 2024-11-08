from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/')
    stock = models.PositiveIntegerField(default=0)  # Stock count

    def __str__(self):
        return self.name
