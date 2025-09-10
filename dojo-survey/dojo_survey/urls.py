
from django.contrib import admin
from django.urls import path
from dojo import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('result/',views.result),
]
