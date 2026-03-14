from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Supplier

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers': suppliers})