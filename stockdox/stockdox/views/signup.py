def handle_request(request):
  form = SignUpForm()
  if request.method == 'POST':
  		form = SignUpForm(request.POST)
  		if form.is_valid():
			  user = form.save()
			  user.email_verified = False
			  username = form.cleaned_data.get('username')
			  password = form.cleaned_data.get('password1')
			  user.save()
			  login(request, user)
			  current_site = get_current_site(request)
			  mail_subject = 'Activate Your StockDox Account'
			  message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
			  to_email = form.cleaned_data.get('email')
			  email = EmailMessage(mail_subject, message, to=[to_email])
			  email.send()
			  return render(request, 'registration/account_activation_prompt.html', {})
  return render(request, 'registration/signup.html', {'form': form})