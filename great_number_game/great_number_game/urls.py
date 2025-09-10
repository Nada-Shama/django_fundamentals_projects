
from django.contrib import admin
from django.urls import path
from number_game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('reset/',views.reset)
]
