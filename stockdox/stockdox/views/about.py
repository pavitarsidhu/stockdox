from django.shortcuts import render, redirect

def handle_request(request):
	return render(request, 'about.html')