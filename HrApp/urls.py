from django.urls import path
from . import views

app_name = 'HrApp'

urlpatterns = [
    path('', views.home_view, name="home_view")
]