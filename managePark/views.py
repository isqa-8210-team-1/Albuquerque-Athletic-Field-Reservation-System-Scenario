from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from parkAvail.models import *
from .forms import *


def park_list(request):
    park = Park.objects.filter(created_date__lte=timezone.now())
    return render(request, 'park_list.html',
                 {'parks': park})


def backend_dashboard(request):
    return render(request, 'backend_dashboard.html')


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
           property.created_date = timezone.now()
           property.save()
           properties = Property.objects.filter(created_date__lte=timezone.now())
           return render(request, 'property_list.html',
                         {'properties': property})
   else:
       form = PropertyForm()
   return render(request, 'property_new.html', {'form': form})
