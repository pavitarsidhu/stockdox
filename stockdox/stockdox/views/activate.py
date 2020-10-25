from django.shortcuts import render, redirect

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from ticker_info.classes.security.tokens import account_activation_token

from ticker_info.models.CustomUser import CustomUser


def handle_request(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.set_email_verified(1)
        user.save()
        login(request, user)
        return render(request, 'registration/account_confirmed.html', {})
    else:
        return render(request, 'registration/invalid_token_link.html', {})