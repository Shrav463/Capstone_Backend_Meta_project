from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking # Ensure Booking is imported
from rest_framework import viewsets # New: Import viewsets for DRF
from .serializers import MenuSerializer, BookingSerializer # New: Import serializers


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data
    }
    return render(request, 'menu.html', main_data)

# Corrected context key to 'menu_item' to match template variable name
def display_menu_items(request, pk=None):
   if pk:
       menu_item = Menu.objects.get(pk=pk)
   else:
       menu_item = " " # Consider handling 'None' case more gracefully for a single item view
   return render(request,'menu.html',{'menu_item': menu_item})


# --- Django REST Framework API ViewSets ---
# These viewsets automatically provide CRUD (Create, Retrieve, Update, Delete) operations
# for your models via API endpoints.

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all() # The set of objects this API will manage
    serializer_class = BookingSerializer # How to convert Booking objects to/from JSON

class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu items to be viewed or edited.
    """
    queryset = Menu.objects.all() # The set of objects this API will manage
    serializer_class = MenuSerializer # How to convert Menu objects to/from JSON