from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('centros/', views.CentroIndexView.as_view(), name='list_all_centros'),
    path('centros/<int:pk>/', views.CentroDetailView.as_view(), name='list_centro'),
    path('centros/<int:id>/editar', views.edit_centro, name='edit_centro'),
    path('estudios/', views.EstudioIndexView.as_view(), name='list_all_estudios'),
    path('estudios/<int:pk>/', views.EstudioDetailView.as_view(), name='list_estudio'),
    path('estudios/<int:id>/editar', views.edit_estudio, name='edit_estudio'),
    path('planes/', views.PlanIndexView.as_view(), name='list_all_planes'),
    path('planes/<int:pk>/', views.PlanDetailView.as_view(), name='list_plan'),
    path('planes/<int:id>/editar', views.edit_plan, name='edit_plan'),
]