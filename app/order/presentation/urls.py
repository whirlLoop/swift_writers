from django.urls import path
from order.presentation.views import PostOrderView
from order.presentation.views import TempMaterialUploadView

app_name = 'order'

urlpatterns = [
    path('', PostOrderView.as_view(), name='order'),
    path('material/', TempMaterialUploadView.as_view(), name='material')
]
