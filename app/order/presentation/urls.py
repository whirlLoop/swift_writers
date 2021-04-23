from django.urls import path
from order.presentation.views import PostOrderView

app_name = 'order'

urlpatterns = [
    path('', PostOrderView.as_view(), name='order')
]
