from django.shortcuts import render
from .models import *
from .forms import *

def park_list(request):
    park = park.objects.filter(created_date__lte=timezone.now())
    return render(request, 'parkAvail/park_list.html',
                 {'parks': park})

def park_new(request):
   if request.method == "POST":
       form = ParkForm(request.POST)
       if form.is_valid():
           park = form.save(commit=False)
           park.created_date = timezone.now()
           park.save()
           parks = park.objects.filter(created_date__lte=timezone.now())
           return render(request, 'parkAvail/park_list.html',
                         {'parks': parks})
   else:
       form = ParkForm()

   return render(request, 'parkAvail/park_new.html', {'form': form})
