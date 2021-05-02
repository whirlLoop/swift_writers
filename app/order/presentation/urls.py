from django.urls import path
from order.presentation.views import PostOrderView
from order.presentation.views import TempMaterialUploadView
from order.presentation.views import TempMaterialDeleteView

app_name = 'order'

urlpatterns = [
    path('', PostOrderView.as_view(), name='order'),
    path('material/', TempMaterialUploadView.as_view(), name='material'),
    path('material/temp/<int:pk>',
         TempMaterialDeleteView.as_view(), name='delete_temp_material')
]
