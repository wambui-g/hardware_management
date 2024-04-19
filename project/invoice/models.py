from django.db import models
from inventory.models import Subcategory, Item

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    count = models.PositiveIntegerField(default=0)
    invoiced_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    FULFILLMENT_CHOICES = (
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    ) 
    fulfillment = models.CharField(max_length=100, choices=FULFILLMENT_CHOICES)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if self.fulfillment == "PAID":
            # Update inventory count if invoice is paid
            item = self.item
            item.count -= self.count
            item.save()
        self.invoiced_amount = self.price * self.count
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number
