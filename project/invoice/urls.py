from django.urls import path
from . import views

urlpatterns = [
        path('invoice/', views.invoice, name='invoice'),
        path('save_invoice/', views.save_invoice, name='save_invoice')
]
