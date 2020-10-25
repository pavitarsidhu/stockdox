from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import FinancialDocuments, CompanyTicker

class StaticViewSitemap(Sitemap):
	protocol = "https"
	def items(self):
		return ['display_about', 'signup', 'display_privacy_policy', 'display_terms_and_conditions']
	def location(self, item):
		return reverse(item)

class CompanyFilingSitemap(Sitemap):
		protocol = "https"
		def items(self):
			return FinancialDocuments.objects.all()

class CompanySitemap(Sitemap):
		protocol = "https"
		def items(self):
			return CompanyTicker.objects.all()