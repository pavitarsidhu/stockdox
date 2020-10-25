from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from itertools import chain

from ticker_info.services.CompanyService import CompanyService

def handle_request(request, id):
	company_service = CompanyService()
	doc = FinancialDocuments.objects.get(id=id)

	context = { 
	'doc' : doc,
	'unique_companies': company_service.get_unique_company_names(),
	'hide_menu': True
	}
	return render(request, 'display_pdf.html', context)