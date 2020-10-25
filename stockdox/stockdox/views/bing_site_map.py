from django.shortcuts import render

def handle_request(request):
	return render(request, 'BingSiteAuth.xml', {})