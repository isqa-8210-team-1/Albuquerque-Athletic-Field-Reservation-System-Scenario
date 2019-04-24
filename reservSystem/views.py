from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from .utils import Calendar
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import *
import calendar
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def prop_event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)

    if request.POST and form.is_valid():
        event = form.save(commit=False)
        event.renter_email = request.user
        event.save()
        new_event = form.save()
        renter_email = request.user.email
        cd = form.cleaned_data
        prop_name = str(cd["prop_name"])
        day = str(cd['day'])
        timeslot = str(cd['timeslot'])
        team_name = str(cd['Team_Name'])
        organization = str(cd['Name_of_the_organization'])

        # set the order in the session
        request.session['event_id'] = new_event.pk
        send_mail(
            'Event Reserved for: ' + prop_name,
            'Reservation details' + '\n\n' + 'Property Name: ' + prop_name + '\n' + 'Day reserved: ' + day + '\n' +
            'Time: ' + timeslot + '\n' + 'Team Name: ' + team_name + '\n' + 'Organization: ' + organization,
            'awesomemsdteam1@gmail.com',
            [renter_email],
            fail_silently=False,
        )
        return redirect(reverse('payment:process'))
    return render(request, 'calendar/prop_event.html', {'form': form})



class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar/prop_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        prop_pk = self.request.GET.get('prop_pk', None)
        prop = get_object_or_404(Prop, pk=prop_pk)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['prop_pk'] = 'prop_pk='+str(prop_pk)
        context['prop_name'] = prop.name
        context['renter_email'] = 'renter_email=' + str(self.request.user)
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(user_id=self.request.user, prop_pk=prop_pk, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def reservation(request, pk):
    propA = get_object_or_404(Event, pk=pk)

    return render(request, 'calendar/reservation.html', {'propEvent': propA})
