from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView, View, ListView

def park_list(request):
    park = Park.objects.filter(created_date__lte=timezone.now())
    return render(request, 'park_list.html',
                 {'parks': park})

def park_new(request):
   if request.method == "POST":
       form = ParkForm(request.POST)
       if form.is_valid():
           park = form.save(commit=False)
           park.created_date = timezone.now()
           park.save()
           parks = park.objects.filter(created_date__lte=timezone.now())
           return render(request, 'park_list.html',
                         {'parks': parks})
   else:
       form = ParkForm()
   return render(request, 'manage_park/park_new.html', {'form': form})

def property_new(request):
   if request.method == "POST":
       form = PropertyForm(request.POST)
       if form.is_valid():
           property = form.save(commit=False)
           property.created_date = timezone.now()
           property.save()
           properties = property.objects.filter(created_date__lte=timezone.now())
   else:
       form = PropertyForm()
   return render(request, 'manage_park/property_new.html', {'form': form})


def properties(request, pk):
    park = get_object_or_404(Park, pk=pk)
    parks = Park.objects.filter(created_date__lte=timezone.now())
    properties = Property.objects.filter(park_name=pk)
    return render(request, 'properties.html', {'parks': parks,
                                                    'properties': properties,})
