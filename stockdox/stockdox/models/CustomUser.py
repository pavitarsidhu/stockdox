from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_paid = models.DateTimeField()
    has_paid = models.BooleanField()
    email_verified = models.BooleanField()

    def set_date_paid(self, date_paid):
        self.date_paid = date_paid

    def get_date_paid(self):
        return self.date_paid

    def set_has_paid(self, has_paid):
        self.has_paid = has_paid

    def get_has_paid(self):
        return self.has_paid

    def set_email_verified(self, email_verified):
        self.email_verified = email_verified

    def get_email_verified(self):
        return self.email_verified

    class Meta:
        managed = False
        db_table = 'auth_user'