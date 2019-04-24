from urllib import request
from .models import *
from .forms import *
from django.shortcuts import redirect,render, get_object_or_404
from .models import FieldCondition
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, ListView


def FieldCondition_list(request):
    fieldCondition = FieldCondition.objects.filter(Report_Time_Date__lte=timezone.now())
    return render(request, 'registration/FieldCondition.html',
                 {'fieldConditions': fieldCondition})

@login_required
def FieldCondition_new(request):
   if request.method == "POST":
       form = FieldConditionForm(request.POST)
       if form.is_valid():
           field = form.save(commit=False)
           field.created_date = timezone.now()
           field.save()
           event = form.cleaned_data["event_id"]
           print(event)
           print(event.id)
           event_obj = Event.objects.get(id=event.id)
           print(event_obj)
           park_name = event_obj.park_name
           prop_name = event_obj.prop_name
           # reserv_no = event_obj.id
           field_obj = FieldCondition.objects.get(id=field.pk)
           field_obj.park_name = park_name
           field_obj.property_name = prop_name
           # field_obj.reservation_number = event.id
           field_obj.save()
           action = "edited"
           print(action)
           return redirect('/FieldCondition_list')
   else:
       form = FieldConditionForm()
   return render(request, 'registration/FieldCondition_Add.html', {'form': form})


@login_required
def FieldCondition_edit(request, pk):
    field = get_object_or_404(FieldCondition, pk=pk)
    if request.method == 'POST':
        # update
        form = FieldConditionForm(request.POST, instance=field)
        if form.is_valid():
            field = form.save(commit=False)
            field.save()
            action = "edited"
            print(action)
            return redirect('/FieldCondition_list')
    else:
        # edit
        form = FieldConditionForm(instance=field)
        return render(request, 'registration/FieldCondition_edit.html', {'form': form})
