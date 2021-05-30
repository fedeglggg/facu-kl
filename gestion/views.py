from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group 

from django.shortcuts import render, redirect
from django.utils.translation import activate
from .models import * 
from .forms import *

def index(request):
	articulos = Articulo.objects.all().order_by('nombre')
	context = {
		'articulos': articulos
	}
	return render(request, 'index.html', context)


def signin(request):
	return render(request, 'signin.html')

def signin_empleado(request):
	# Cambiar idioma de los errores
	activate('es')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()	
			try:
				group = Group.objects.get(name='empleados')
			except Group.DoesNotExist:
				group = Group(name='empleados')
				group.save()
			user.groups.add(group)
			return redirect('index')
		else:
			# Al remover todos los atributos asignados por widgets envio form con errores y form nueva
			new_form = RegisterForm()
			follow_up_form = zip(form, new_form)
			context = {
				'follow_up_form': follow_up_form
			}
			print(context)	
	else:
		form = RegisterForm()
		context = {
			'form': form
		}
	return render(request, 'signin_empleado.html', context)

# Nombre para que no choque con import login
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			mensaje = 'La combinación de usuario y contraseña no es valida'
			context = {
				'mensaje_error': mensaje
			}
			return render(request, 'login.html', context)
	return render(request, 'login.html')

def empleados(request):
	if request.method == 'GET':
		empleados = User.objects.filter(groups__name='empleados')
		context = {
			'empleados': empleados
		}
		print(empleados)
		return render(request, 'empleados.html', context)

def adm(request):
	return render(request, 'adm/index.html')
