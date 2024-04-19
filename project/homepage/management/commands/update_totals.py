from django.core.management.base import BaseCommand
from inventory.models import Subcategory, Item
from homepage.models import Totals
from django.db.models import Sum
from django.db import models

class Command(BaseCommand):
    help = 'Updates total counts for each subcategory'

    def handle(self, *args, **kwargs):
        for subcategory in Subcategory.objects.all():
            total_count = Item.objects.filter(subcategory=subcategory).aggregate(total_count=models.Sum('count'))['total_count'] or 0
            Totals.objects.update_or_create(subcategory=subcategory, defaults={'total_count': total_count})
        self.stdout.write(self.style.SUCCESS('Totals updated successfully'))
