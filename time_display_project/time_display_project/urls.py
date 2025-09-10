from django.contrib import admin
from django.urls import path
from time_display import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),                
    path('display_time/', views.index ) ,
]
