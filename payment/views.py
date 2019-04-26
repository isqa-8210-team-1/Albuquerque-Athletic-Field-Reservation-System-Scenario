import braintree
from django.shortcuts import render, redirect, get_object_or_404
from reservSystem.models import Event
from parkAvail.models import *

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def payment_process(request):
    event_id = request.session.get("event_id")
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        #print('inside post method')
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction

        result = braintree.Transaction.sale({
            'amount': '10',  # create a new amount field  #format(Prop.price)
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True  #give false pending payment
            }
        })
        if result.is_success:
            # mark the order as paid
            #print('inside success')
            event.paid = True
            # store the unique transaction id
            event.braintree_id = result.transaction.id
            event.save()

            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        #print('get method')
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'event': event,
                       'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
