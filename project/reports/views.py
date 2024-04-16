from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def reports(request):
    template = loader.get_template("reports.html")
    return HttpResponse(template.render())
