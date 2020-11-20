__author__ = 'Rodrigo.Oliveira'

from core import views
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.control),

    # Policial
    path('policial/edit/', views.edit_policial, name='edit_policial'),
    path('policial/save/', views.save_policial, name='save_policial'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
