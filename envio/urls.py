from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('centros', views.list_all_centros, name='list_all_centros'),
    path('centros/<int:id>/', views.list_centro, name='list_centro'),
    path('centros/<int:id>/editar', views.edit_centro, name='edit_centro'),
    #path('centros/<int:id>/borrar', views.delete_centro, name='delete_centro'),
    path('estudios', views.list_all_estudios, name='list_all_estudios'),
    path('estudios/<int:id>/', views.list_estudio, name='list_estudio'),
    path('estudios/<int:id>/editar', views.edit_estudio, name='edit_estudio'),
    #path('estudios/<int:id>/borrar', views.delete_estudio, name='delete_estudio'),
    path('planes', views.list_all_planes, name='list_all_planes'),
    path('planes/<int:id>/', views.list_plan, name='list_plan'),
]