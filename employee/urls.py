from . import views
from django.urls import path

app_name = 'employee'

urlpatterns = [
    path('<emp_id>/profile/', views.employee_profile, name="employee_profile"),
    path('all/', views.all_employees, name="all_employees"),
]