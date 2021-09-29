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
    # google auth
    path('33', TemplateView.as_view(template_name="googleaouth.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)