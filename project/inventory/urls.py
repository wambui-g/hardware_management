from django.urls import path
from . import views

urlpatterns = [
        path('inventory/', views.inventory, name='inventory'),
        path('save_inventory/', views.save_inventory, name='save_inventory')
]
