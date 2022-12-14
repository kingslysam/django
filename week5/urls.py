"""week5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from CMS.views import customer, transaction, CustomerAdd, CustomerDetails, CustomerFormDjango, \
    CMISHomeView, CustomerMobile

urlpatterns = [
    path('', CMISHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('customer/', customer, name='customer'),
    path('transaction/', transaction),
    path('add/', CustomerAdd.as_view(), name='customer-add'),
    path('customer/profile<int:pk>', CustomerDetails.as_view(), name='customer-profile'),
    path('edit/', CustomerFormDjango.as_view(), name='edit'),
    # path('profile/', CustomerListView.as_view(), name='profile'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('customer/mobile<int:pk>', CustomerMobile.as_view(), name='mobile')
]
