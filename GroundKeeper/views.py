from urllib import request
from .models import *
from .forms import *
from django.shortcuts import redirect,render, get_object_or_404
from .models import FieldCondition
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, ListView


def FieldCondition_list(request):
    fieldCondition = FieldCondition.objects.filter(created_date__lte=timezone.now())
    return render(request, 'registration/FieldCondition.html',
                 {'fieldConditions': fieldCondition})

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
            # return render(request, 'registration/FieldCondition.html', {'field_form': field, 'action': action})
    else:
        # edit
        form = FieldConditionForm(instance=field)
        return render(request, 'registration/FieldCondition_edit.html', {'form': form})
