from . import views
from django.urls import path

app_name = 'brand'

urlpatterns = [
    path('<brand_id>/details/', views.brand_details, name='brand_details'),
    path('all/', views.all_brands, name='all_brands')
]