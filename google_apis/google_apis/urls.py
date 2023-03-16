from django.contrib import admin
from django.urls import path

from orders.views import data_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', data_view, name='data'),
]

