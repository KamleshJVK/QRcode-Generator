from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    
    path('get_code', views.get_code, name='get_code'),
] 