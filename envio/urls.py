from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('centros', views.list_all_centros, name='list_all_centros'),
    path('centros/<int:id>/', views.list_centro, name='list_centro'),
]