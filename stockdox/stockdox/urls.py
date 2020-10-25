from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap

from ticker_info.sitemap import StaticViewSitemap, CompanyFilingSitemap, CompanySitemap

from ticker_info.views import (
  activate, 
  about, 
  bing_site_map, 
  checkout, 
  company_pdf, 
  home, 
  privacy_policy, 
  profile, 
  search_company, 
  signup, 
  terms_and_conditions)

sitemaps = {
 'pages': StaticViewSitemap,
 'companies': CompanySitemap
}

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/signup/', signup.handle_request, name='signup'),
  re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate.handle_request, name='activate'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('', home.handle_request, name='home'),
  path('search/<str:search_value>/', search_company.handle_request, name='search_company'),
  path('view/<int:id>/', company_pdf.handle_request, name='display_pdf'),
  path('privacy-policy/', privacy_policy.handle_request, name='display_privacy_policy'),
  path('terms-and-conditions/', terms_and_conditions.handle_request, name='display_terms_and_conditions'),
  path('about/', about.handle_request, name='display_about'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
  path('checkout/', checkout.handle_request, name='checkout'),
  path('BingSiteAuth.xml', bing_site_map.handle_request, name='bingSiteAuth'),
  path('profile/', profile.handle_request, name='profile')
]
