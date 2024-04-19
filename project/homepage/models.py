from django.db import models
from inventory.models import Category, Subcategory, Item

class Totals(models.Model):
    subcategory = models.OneToOneField(Subcategory, on_delete=models.CASCADE)
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.subcategory} - Total Count: {self.total_count}"
