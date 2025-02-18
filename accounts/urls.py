from . import views
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name = 'register_view'),
    path('login/', views.login_view, name = 'login_view'),
    path('logout/', views.logout_view, name = 'logout_view'),

]
