from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings

import stripe
import datetime

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def handle_request(request):
	user = request.user
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	error = ""
	if request.method == 'POST':
		token = request.POST['stripeToken']
		try:
			charge = stripe.Charge.create(
			  amount=24000,
			  currency='cad',
			  description="StockDox annual subscription purchase for user " + request.user.username,
			  source=token,
			)
			user.set_has_paid(1)
			user.set_date_paid(datetime.datetime.now())
			user.save()
			context = {'user': user}
			return render(request, 'payment/payment-processed.html', context)
		except stripe.error.CardError as e:
			error = e.error.message
			print(error)
	context = {'publishKey': publishKey, 'error': error }
	template = 'payment/checkout.html'
	return render(request, template, context)