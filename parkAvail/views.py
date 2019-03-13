from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView, View, ListView


def park_list(request):
    park = Park.objects.filter(created_date__lte=timezone.now())
    # properties = Property.objects.filter(park).count(park)
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
        return render(request, 'manage_park/park_new.html', {'form': form})


def property_details(request):
    prop = Property.objects.filter(created_date__lte=timezone.now())
    return render(request, 'properties.html', {'properties': prop})


def property_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.created_date = timezone.now()
            property.save()
            properties = property.objects.filter(created_date__lte=timezone.now())
            return render(request, 'properties.html',
                          {'properties': property})
    else:
        form = PropertyForm()
        return render(request, 'manage_park/property_new.html', {'form': form})


def propertiess(request, park_slug=None):
    park = None
    parks = Park.objects.all()
    properties = Property.objects.filter()
    if park_slug:
        park = get_object_or_404(Park, slug=park_slug)
        #products = products.filter(park=park)
    return render(request, 'properties.html',
                  {'park': park,
                   'parks': parks,
                   'properties': properties, })


def property_detailsss(request, id, slug):
    property = get_object_or_404(Property, id=id, slug=slug)
    return render(request, 'properties.html', {'property': property})




