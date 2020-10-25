from django.db import models

class FinancialDocuments(models.Model):
    companyname = models.CharField(db_column='companyName', max_length=100)  # Field name made lowercase.
    documenttype = models.CharField(db_column='documentType', max_length=500)  # Field name made lowercase.
    timestamp = models.BigIntegerField(db_column='timeStamp')  # Field name made lowercase.
    dateoffilling = models.CharField(db_column='dateOfFilling', max_length=100)  # Field name made lowercase.
    timeoffilling = models.CharField(db_column='timeOfFilling', max_length=100)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=100)  # Field name made lowercase.
    fileformat = models.CharField(db_column='fileFormat', max_length=300)  # Field name made lowercase.
    filesize = models.CharField(db_column='fileSize', max_length=100)  # Field name made lowercase.
    sedarurl = models.CharField(db_column='SedarURL', unique=True, max_length=500)  # Field name made lowercase.
    url = models.CharField(max_length=500)
    storageid = models.CharField(db_column='storageID', max_length=500)  # Field name made lowercase.
    
    def get_absolute_url(self):
        return f'/view/{self.storageid}'

    class Meta:
        managed = False
        db_table = 'financial_documents'