import requests
import re

from ticker_info.models.FinancialDocuments import FinancialDocuments, CompanyTicker

class CompanyService:
	def get_unique_company_names(self):
		return CompanyTicker.objects.order_by('companyname')

	def get_stock_price(self, ticker):
		url = "https://web.tmxmoney.com/quote.php?qm_symbol=" + ticker
		price = ''
		try:
			html = requests.get(url).text
			element_with_price = re.search('<span>(.+?)</span>', html)
			if element_with_price is not None:
				element_with_price = element_with_price.group(0)
				price = '$' + element_with_price.replace('<span>', '').replace('</span>', '')
		except Exception as e:
			pass
		return price

	def populate_name_and_ticker(self, search_value, ticker, name):

		# NOTE: The UI provides a smart search where it auto fills the correct format upon typing
		# There are 3 formats supported by the search:
			# 1. "TICKER  : company name" format
			# 2. only company name
			# 3. only ticker 

		name_and_ticker = search_value.lower().split(":", 1)
		company_found = False

		# case 1
		if len(name_and_ticker) == 2:
			name = name_and_ticker[1].strip()
			ticker = name_and_ticker[0].strip()

			if FinancialDocuments.objects.filter(companyname = name).exists():
				company_found = True
				ticker = self.get_ticker_from_company_name(name)
			elif CompanyTicker.objects.filter(ticker = ticker).exists():
				company_found = True
				company_ticker = CompanyTicker.objects.get(ticker = ticker)
				name = company_ticker.companyname

		if not company_found and FinancialDocuments.objects.filter(companyname = search_value).exists():
			# case 2
			name = search_value
			ticker = self.get_ticker_from_company_name(name)
		elif not company_found and CompanyTicker.objects.filter(ticker = search_value).exists():
			# case 3
			company_ticker = CompanyTicker.objects.get(ticker = search_value)
			name = company_ticker.companyname
			ticker = company_ticker.ticker

	def get_ticker_from_company_name(self, name):
		tickers = CompanyTicker.objects.filter(companyname__iexact = name)
		if tickers.count() >= 1:
			company_ticker = tickers.first()
			return company_ticker.ticker

	def generate_docs_dict(self, documents):
		# TODO: Restructure with more optimal way for fetching / organizing documents.

		quarterly_docs = documents.filter(documenttype="financial statements", filename="Interim financial statements/report - English").order_by("-timestamp")
		quarterly_docs_with_name_variation = documents.filter(documenttype="financial statements", filename="Interim financial statements - English").order_by("-timestamp")
		news_docs = documents.filter(documenttype="news releases", filename="News release - English").order_by("-timestamp")
		annual_docs = documents.filter(documenttype="annual report", filename="Annual report - English").order_by("-timestamp")
		audited_annual_docs = documents.filter(documenttype="financial statements", filename="Audited annual financial statements - English").order_by("-timestamp")
		proxy_docs = documents.filter(documenttype="proxy circular", filename="Management information circular - English").order_by("-timestamp")
		proxy_docs_with_nam_variation = documents.filter(documenttype="proxy circular", filename="Management proxy / information circular - English (BC, ON - Form 30, QC)").order_by("-timestamp")
		management_docs = documents.filter(documenttype="management's discussion & analysis", filename="MD&A - English").order_by("-timestamp")
		annual_info_form_docs = documents.filter(documenttype="annual information form", filename="Annual information form - English").order_by("-timestamp")
		annual_info_form_docs_with_name_var = documents.filter(documenttype="annual information form", filename="Renewal annual information form - English").order_by("-timestamp")
		earl_warn_docs = documents.filter(documenttype="early warning report").order_by("-timestamp")
		mat_change_docs = documents.filter(documenttype="material change report", filename="Material change report - English").order_by("-timestamp")
		prospectus_docs = documents.filter(documenttype="prospectus", filename__contains="prospectus").order_by("-timestamp")
		tech_report_docs = documents.filter(documenttype="Technical report - ni 43-101", filename='Technical report (NI 43-101) - English').order_by("-timestamp")

		other_docs = sorted(list(chain(earl_warn_docs, mat_change_docs)), key=lambda x: x.timestamp, reverse=True)
		quarterly_docs = sorted(list(chain(quarterly_docs, quarterly_docs_with_name_variation)), key=lambda x: x.timestamp, reverse=True)
		proxy_docs = sorted(list(chain(proxy_docs, proxy_docs_with_nam_variation)), key=lambda x: x.timestamp, reverse=True)
		annual_info_form_docs = sorted(list(chain(annual_info_form_docs, annual_info_form_docs_with_name_var)), key=lambda x: x.timestamp, reverse=True)

		return {
			"quarterly_docs" : quarterly_docs,
			"quarterly_docs_with_name_variation" : quarterly_docs_with_name_variation,
			"news_docs" : news_docs,
			"annual_docs": annual_docs,
			"audited_annual_docs" : audited_annual_docs,
			"proxy_docs" : proxy_docs,
			"proxy_docs_with_nam_variation" : proxy_docs_with_nam_variation,
			"management_docs" : management_docs,
			"annual_info_form_docs" : annual_info_form_docs,
			"annual_info_form_docs_with_name_var": annual_info_form_docs_with_name_var,
			"earl_warn_docs" : earl_warn_docs,
			"mat_change_docs" : mat_change_docs,
			"prospectus_docs" : prospectus_docs,
			"tech_report_docs" : tech_report_docs,
			"other_docs" : other_docs
		}