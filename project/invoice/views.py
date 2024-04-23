from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Invoice
from inventory.models import Subcategory, Item
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect


def invoice(request):
    # Retrieve all invoices from the database
    subcategories = Subcategory.objects.all()
    items = Item.objects.all()
    invoices = Invoice.objects.all()

    # Pass the invoices to the template context
    context = {'subcategories': subcategories, 'items': items, 'invoices': invoices}
    
    # Render the invoice template with the invoices data
    return render(request, 'invoice.html', context)
    
def save_invoice(request):
    if request.method == 'POST':
        # Retrieve data from the form
        invoice_number = request.POST.get('invoicenumberInput')
        subcategory_id = request.POST.get('subCategoryInput') 
        item_id = request.POST.get('itemInput')
        price = float(request.POST.get('priceInput'))
        count = int(request.POST.get('countInput'))
        fulfillment = request.POST.get('fulfillmentInput')
        date = request.POST.get('dateInput')

        # Retrieve the Item instance based on the provided item ID
        item = get_object_or_404(Item, pk=item_id)
        subcategory = get_object_or_404(Subcategory, pk=subcategory_id)

        # Calculate the invoiced amount
        invoiced_amount = price * count

        # Create a new invoice object and save it to the database
        new_invoice = Invoice(invoice_number=invoice_number, subcategory=subcategory, item=item, price=price, count=count,
                              invoiced_amount=invoiced_amount, fulfillment=fulfillment, date=date)
        new_invoice.save()

        # Add a success message
        messages.success(request, 'Invoice saved successfully!')

        # Redirect to a success page or reload the current page
        # You can customize this according to your needs
        return HttpResponseRedirect('/invoice/')  # Redirect to the invoices page after saving

    # If the request method is not POST, handle other cases here (e.g., GET request)

    # Render a template or return a response as needed
    # For example, you can render a blank page or a confirmation message
    # return render(request, 'invoices/success.html')  # Render a success page after saving

    # Instead of rendering a success template, you can redirect back to the form page with a success message
    return HttpResponseRedirect('/invoice/')

def logout_user(request):
    logout(request)
    return redirect('login') 