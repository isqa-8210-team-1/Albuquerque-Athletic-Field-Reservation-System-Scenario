from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from parkAvail.models import *
from .forms import *


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
           parks = Park.objects.filter(created_date__lte=timezone.now())
           return render(request, 'park_list.html',
                         {'parks': parks})
   else:
       form = ParkForm()
   return render(request, 'park_new.html', {'form': form})


def park_edit(request, pk):
   park = get_object_or_404(Park, pk=pk)
   if request.method == "POST":
       # update
       form = ParkForm(request.POST, instance=park)
       if form.is_valid():
           park = form.save(commit=False)
           park.updated_date = timezone.now()
           park.save()
           park = Park.objects.filter(created_date__lte=timezone.now())
           return render(request, 'park_list.html',
                         {'parks': park})
   else:
        # edit
       form = ParkForm(instance=park)
   return render(request, 'park_edit.html', {'form': form})


def park_delete(request, pk):
    park = get_object_or_404(Park, pk=pk)
    park.delete()
    return redirect('park_list')


def property_new(request):
   if request.method == "POST":
       form = PropertyForm(request.POST)
       if form.is_valid():
           property = form.save(commit=False)
           property.created = timezone.now()
           property.save()
           property = Prop.objects.filter(created__lte=timezone.now())
           return render(request, 'property.html',
                         {'properties': property})
   else:
       form = PropertyForm()
   return render(request, 'property_new.html', {'form': form})

def property(request, pk):
    parks = Park.objects.filter(created_date__lte=timezone.now())
    if pk > 0 :
        park = get_object_or_404(Park, pk=pk)
        properties = Prop.objects.filter(park_under=pk)
    else:
        properties = Prop.objects.filter(created__lte=timezone.now())

    return render(request, 'property.html', {'parks': parks,
                                            'properties': properties
                                        })

def property_edit(request, pk, pp):
   park = get_object_or_404(Prop, pk=pk)
   if request.method == "POST":
       # update
       form = PropertyForm(request.POST, instance=park)
       if form.is_valid():
           property = form.save(commit=False)
           property.updated_date = timezone.now()
           property.save()
           property = Prop.objects.filter(park_under=pp)
           return render(request, 'property.html',
                         {'properties': property})
   else:
        # edit
       form = PropertyForm(instance=park)
   return render(request, 'property_edit.html', {'form': form})

def property_delete(request, pk, pp):
    Property = get_object_or_404(Prop, pk=pk)
    Property.delete()
    properties = Prop.objects.filter(park_under=pp)
    return render(request, 'property.html',
                  {'properties': properties})
