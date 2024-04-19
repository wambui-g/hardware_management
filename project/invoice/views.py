from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Invoice


def invoice(request):
    # Retrieve all invoices from the database
    invoices = Invoice.objects.all()

    # Pass the invoices to the template context
    context = {'invoices': invoices}
    
    # Render the invoice template with the invoices data
    return render(request, 'invoice.html', context)
