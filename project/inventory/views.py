from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Subcategory, Item
import json

def inventory(request):
    items = Item.objects.all()

    # Pass the items to the template context
    context = {'items': items}

    # Render the inventory template with the items
    return render(request, 'inventory.html', context)

def save_inventory(request):
     return JsonResponse({'success': False, 'error': 'Invalid request method'})