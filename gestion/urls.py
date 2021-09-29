from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'),
    path('registrar/', views.signin, name='signin'),
    path('registrar-empleado/', views.signin_empleado, name='signin_empleado'),
    path('empleados/', views.empleados, name='empleados'),
    path('gestion/', views.gestion, name='gestion'),
]
