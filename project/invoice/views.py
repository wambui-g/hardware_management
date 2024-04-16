from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def invoice(request):
    template = loader.get_template("invoice.html")
    return HttpResponse(template.render())
