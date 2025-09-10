
from django.contrib import admin
from django.urls import path
from counter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('destroy_session/',views.destroy_session),
]
