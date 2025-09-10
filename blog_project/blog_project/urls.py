

from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new',views.new),
    path('blogs/create',views.create),
    path('blogs/<int:num>',views.show),
    path('edit/<int:num>',views.edit),
    path('blogs/<int:num>/delete',views.destroy),
    path('blogs/json',views.json),
]
