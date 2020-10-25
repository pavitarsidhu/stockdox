from django import forms
from ticker_info.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=200, )
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def clean_email(self):
		# Get the email
		email = self.cleaned_data.get('email')

		# Check to see if any users already exist with this email as a username.
		try:
			match = CustomUser.objects.get(email=email)
		except CustomUser.DoesNotExist:
			# Unable to find a user, this is fine
			return email

		# A user was found with this as a username, raise an error.
		raise forms.ValidationError('This email address is already in use.')