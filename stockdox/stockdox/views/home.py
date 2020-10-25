from django.shortcuts import render, redirect

def handle_request(request):
	company_service = CompanyService()
	context = {'unique_companies': company_service.get_unique_company_names()}
	return render(request, 'home.html', context)