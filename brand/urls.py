from . import views
from django.urls import path

app_name = 'brand'

urlpatterns = [
    path('', views.brand_details, name= 'brand_details'),
    path('', views.all_brands, name= 'all_brands')
]