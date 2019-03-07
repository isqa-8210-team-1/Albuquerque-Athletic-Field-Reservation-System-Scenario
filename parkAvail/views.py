from django.shortcuts import render
from .models import *

def park_list(request):
    park = park.objects.filter(created_date__lte=timezone.now())
    return render(request, 'parkAvail/park_list.html',
                 {'parks': park})
