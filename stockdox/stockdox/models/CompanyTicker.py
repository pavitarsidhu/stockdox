from django.db import models

from six.moves.urllib.parse import urlencode, quote

class CompanyTicker(models.Model):
    companyname = models.CharField(db_column='companyName', unique=True, max_length=100)  # Field name made lowercase.
    ticker = models.CharField(unique=True, max_length=500)

    def get_absolute_url(self):
        company_name_in_url_format = quote(self.companyname)
        return f'/search/{company_name_in_url_format}'

    class Meta:
        managed = False
        db_table = 'company_ticker'