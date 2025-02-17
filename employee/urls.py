from . import views
from django.urls import path

app_name = 'employee'

urlpatterns = [
    path('', views.employee_profile, name="employee_profile")
]