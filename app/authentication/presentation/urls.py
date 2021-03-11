from django.urls import path
from authentication.presentation.views.account_activation import AccountActivationView

app_name = 'authentication'

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>/',
         AccountActivationView.as_view(), name='activate')
]
