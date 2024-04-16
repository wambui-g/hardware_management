from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inventory(request):
    template = loader.get_template("inventory.html")
    return HttpResponse(template.render())
