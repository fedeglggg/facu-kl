from django.contrib import admin
from django.urls import path
from . import views
# auth
from django.urls import include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'),
    # path('registrar/', views.signin, name='signin'),
    # path('registrar-empleado/', views.signin_empleado, name='signin_empleado'),
    path('nuevo-empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('empleados/', views.empleados, name='empleados'),
    path('gestion/', views.gestion, name='gestion'),
    path('armar-pc/', views.armar_pc, name='armar_pc'),
    # oauth
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

# path('accounts/', include('allauth.urls')) picks up urls from the lib unless they get overwritten 
# at project/templates 
