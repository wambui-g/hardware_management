from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inventory.models import Category

def homepage(request):
    # Retrieve all categories with their related subcategories and totals
    categories = Category.objects.prefetch_related('subcategories').all()

    context = {'categories': categories}
    return render(request, 'homepage.html', context)
