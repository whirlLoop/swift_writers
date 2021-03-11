from django.views import View
from django.shortcuts import render, redirect
from authentication.token import account_activation_token
from django.contrib.auth import get_user_model


class AccountActivationView(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.pop('uidb64')
        token = kwargs.pop('token')
        user_model = get_user_model()
        user = user_model.objects.get_user_by_uid(uidb64)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('/login')
        return render(request, 'registration/account_activation_invalid.html')
