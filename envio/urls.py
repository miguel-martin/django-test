from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
import private_storage.urls # refer to https://github.com/edoburu/django-private-storage

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
    path('personas/', views.PersonaIndexView.as_view(), name='list_all_personas'),
    path('personas/<int:pk>/', views.PersonaDetailView.as_view(), name='list_persona'),
    path('matriculas/', views.MatriculaIndexView.as_view(), name='list_all_matriculas'),
    path('matriculas/<int:pk>/', views.MatriculaDetailView.as_view(), name='list_matricula'),
    path('entregas/', views.EntregaIndexView.as_view(), name='list_all_entregas'),
    path('entregas/<int:pk>/', views.EntregaDetailView.as_view(), name='list_entrega'),
    path('entregas/<int:pk>/editar/', views.edit_or_create_Entrega, name='edit_create_entrega'),
    path('entregas/<int:pk>/borrar/', views.delete_Entrega, name='delete_entrega'),
    path('entregas/nueva/', views.edit_or_create_Entrega, name='edit_create_entrega'),
    path('micuenta/', views.user_view, name='micuenta'),
    path('login/', auth_views.LoginView.as_view(template_name='envio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('i18n/', include('django.conf.urls.i18n'), name='set_language'), # refer to https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#set-language-redirect-view
    path('descargar-memoria/<int:pk>', views.MemoriaDownloadView.as_view(), name='download-memoria'), # refer to https://github.com/edoburu/django-private-storage
    path('descargar-anexos/<int:pk>', views.AnexosDownloadView.as_view(), name='download-anexos'), # refer to https://github.com/edoburu/django-private-storage
]

# To add private files (refer to https://django-private-files.readthedocs.io/en/latest/)
urlpatterns += [path('private-media/', include('private_storage.urls'))]

# To add debug bar. refer to https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
if settings.DEBUG:
    # DEBUG TOOLBAR
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # MEDIA ACCESS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)