from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Subcategory, Item
import json
from django.contrib import messages 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout

def inventory(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    items = Item.objects.all()

    # Pass the items to the template context
    context = {'categories': categories, 'subcategories': subcategories, 'items': items}

    # Render the inventory template with the items
    return render(request, 'inventory.html', context)

def save_inventory(request):
    if request.method == 'POST':
        # Retrieve data from the form
        #category = request.POST.get('categoryInput')
        subcategory_id = request.POST.get('subCategoryInput')
        item_name = request.POST.get('nameInput')
        count = int(request.POST.get('countInput'))

        # Retrieve the subcategory instance based on the provided item ID
        subcategory = get_object_or_404(Subcategory, pk=subcategory_id)

        # Check if an item with the same name and subcategory already exists
        existing_item = Item.objects.filter(name=item_name, subcategory__name=subcategory).first()

        if existing_item:
            # If an item already exists, increase its count
            existing_item.count += count
            existing_item.save()
        else:
            # If the item doesn't exist, create a new one
            subcategory = get_object_or_404(Subcategory, name=subcategory)
            new_item = Item(subcategory=subcategory, name=item_name, count=count)
            new_item.save()

        # Redirect to a success page or reload the current page
        # You can customize this according to your needs
        return HttpResponseRedirect('/inventory/')  # Redirect to the inventory page after saving

    # If the request method is not POST, handle other cases here (e.g., GET request)

    # Render a template or return a response as needed
    # For example, you can render a blank page or a confirmation message
    return HttpResponseRedirect('/inventory/')  

def logout_user(request):
    logout(request)
    return redirect('login') 