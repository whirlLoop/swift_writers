from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.forms.login_form import LoginForm
from authentication.presentation.views import (
    AccountActivationView, UserProfileView, AvatarUpdateView)


app_name = 'authentication'

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>/',
         AccountActivationView.as_view(), name='activate'),
    path('accounts/login/',
         auth_views.LoginView.as_view(
             authentication_form=LoginForm, redirect_authenticated_user=True),
         name='login'),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('accounts/profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')
]
