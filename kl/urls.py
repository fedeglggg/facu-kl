from django.contrib import admin
from django.urls import path, include
from . import settings
# Para el path de ImageField
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
# auth
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)