from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uses = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 11)])
    characters = models.CharField(max_length=255)

    def __str__(self):
        return self.name
