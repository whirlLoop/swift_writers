from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.forms.login_form import LoginForm
from authentication.presentation.views.account_activation import (
    AccountActivationView)


app_name = 'authentication'

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>/',
         AccountActivationView.as_view(), name='activate'),
    path('accounts/login/',
         auth_views.LoginView.as_view(authentication_form=LoginForm),
         name='login'),
]
