from django.shortcuts import redirect, render, get_object_or_404
from .models import MyUser
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from .forms import *
from django.contrib.auth.decorators import login_required


def HomePageView(request):
   return render(request, 'base.html')

def home(request):
   return render(request, 'home.html',
                 {'account': home})

def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/signup_done.html', {'new_user': new_user})
    else:
        user_form = SignupForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})

def registerFullProfile(request):
    if request.method == 'POST':
        user_form = RegistrationFullForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # ---- if a user is created by an employee, redirect it to reservation page
            return render(request, 'registration/signup_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationFullForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

@login_required
def profile_edit(request, pk):
   user = get_object_or_404(MyUser, pk=pk)
   if request.method == "POST":
      # update
      form = UpdateProfileForm(request.POST, instance=user)
      if form.is_valid():
          user = form.save(commit=False)
          user.save()
          action = "edited"
          return render(request, 'registration/profile_view.html', {'user_form': user, 'action': action})
   else:
       # edit
    form = UpdateProfileForm(instance=user)
   return render(request, 'registration/profile_edit.html', {'form': form})


@login_required
def profile_view(request, pk):
   user = get_object_or_404(MyUser, pk=pk)
   return render(request, 'registration/profile_view.html', {'user_form': user})


def contact(request):
    form_class = ContactForm

    return render(request, 'registration/contact.html', {'form': form_class})

def FAQ(request):
 return render(request, 'registration/FAQ.html', {'registration': FAQ})


