from django.shortcuts import render, redirect
from itertools import chain

from ticker_info.models.FinancialDocuments import FinancialDocuments
from ticker_info.services.CompanyService import CompanyService
from ticker_info.models.CompanyTicker import CompanyTicker

def handle_request(request, search_value):
	company_service = CompanyService()

	name_and_ticker = search_value.split(":", 1)
	name = ""
	ticker = ""

	company_service.populate_name_ticker(search_value, ticker, name);

	documents = FinancialDocuments.objects.none()
	if name is not None:
		documents = FinancialDocuments.objects.filter(companyname = name)

	docs_dict = company_service.generate_docs_dict(documents)

	context = {
	'company_name': name,
	'ticker': ticker,
	'quarterly_docs': docs_dict.get('quarterly_docs'),
	'annual_docs': docs_dict.get('annual_docs'),
	'audited_annual_docs': docs_dict.get('audited_annual_docs'),
	'news_docs': docs_dict.get('news_docs'),
	'proxy_docs': docs_dict.get('proxy_docs'),
	'management_docs': docs_dict.get('management_docs'),
	'other_docs': docs_dict.get('other_docs'),
	'annual_info_form_docs': docs_dict.get('annual_info_form_docs'),
	'prospectus_docs': docs_dict.get('prospectus_docs'),
	'tech_report_docs': docs_dict.get('tech_report_docs'),
	'unique_companies': company_service.get_unique_company_names(),
	'stock_price': company_service.get_stock_price(ticker),
	'num_tech_reports': len(docs_dict.get('tech_report_docs')),
	'annual_docs_count': len(docs_dict.get('annual_docs')),
	'prospectus_docs_count': len(docs_dict.get('prospectus_docs')),
	'news_docs_count': len(news_docs)
	}

	return render(request, 'display_company.html', context)