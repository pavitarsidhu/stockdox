from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta

@login_required
def handle_request(request):
	user = request.user
	expiration_date = None;
	if user.get_date_paid() is not None:
		expiration_date = user.get_date_paid() + relativedelta(years=1) 
	context = {'user': user, 'expiration_date': expiration_date}
	template = 'registration/profile.html'
	return render(request, template, context)