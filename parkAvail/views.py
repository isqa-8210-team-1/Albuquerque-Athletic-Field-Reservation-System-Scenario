from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView, View, ListView


def prop_list(request, park_slug=None):
    park = None
    parks = Park.objects.all()
    props = Prop.objects.filter(available=True)
    if park_slug:
        park = get_object_or_404(Park, slug=park_slug)
        props = props.filter(park_under=park)
    return render(request,
                  'prop_list.html',
                  {'park': park,
                   'parks': parks,
                   'props': props})


def prop_detail(request, id, slug):
    prop = get_object_or_404(Prop,
                             id=id,
                             slug=slug,
                             available=True)
    # cart_product_form = CartAddProductForm()
    return render(request,
                  'prop_detail.html',
                  {'prop': prop})


