from django.urls import path

from api.customer.views import CustomerCreateAPIView, CustomerListAPIView, CustomerUpdateAPI, CustomerDeleteAPI, CustomerFull
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CMIS API')

urlpatterns = [
    path('create', CustomerCreateAPIView.as_view(), name='create'),
    path('list', CustomerListAPIView.as_view(), name='list'),
    path('update', CustomerUpdateAPI.as_view(), name='update'),
    path('delete', CustomerDeleteAPI.as_view(), name='delete'),
    path('<int:pk>', CustomerFull.as_view(), name='full'),
    path('swagger', schema_view)
]
