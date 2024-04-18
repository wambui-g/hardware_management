from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
