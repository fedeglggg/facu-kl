from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.models import Group 

from django.shortcuts import render, redirect
from django.utils.translation import activate
from .models import * 
from .forms import *

from django.http import HttpResponse

def index(request):
	articulos = Articulo.objects.all().order_by('nombre')
	context = {
		'articulos': articulos
	}
	return render(request, 'index.html', context)

def gestion(request):
	user = request.user
	if es_empleado(user):
		print('yes')
		return render(request, 'gestion_main.html')
	else:
		return redirect('index')
	

def signin(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['email']
			if User.objects.filter(username=username).exists():
				context = {
					'error_message': 'Ya existe un usuario registrado con este email',
					'form': form
				}
				return render(request, 'signin.html', context)
			else:
				password = form.cleaned_data['password1']
				password2 = form.cleaned_data['password2']
				if password != password2:
					context = {
						'error_message': 'Las constraseñas no coinciden',
						'form': form
					}
					return render(request, 'signin.html', context)
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				new_user = User(username=username, password=password, first_name=first_name, last_name=last_name) 
				new_user.save()
				try:
					group = Group.objects.get(name='clientes')
				except Group.DoesNotExist:
					group = Group(name='clientes')
					group.save()
				new_user.groups.add(group)
				form = RegisterForm()
				context = {
					'success_message': 'Usuario creado correctamente',
					'form': form
				}
				return render(request, 'signin.html', context)

		else:
			form = RegisterForm()
			context = {
				'error_message': 'La información no es valida, porfavor intente nuevamente',
				'form': form
			}
			return render(request, 'signin.html', context)
	else:
		form = RegisterForm()
		context = {
			'form': form
		}
	return render(request, 'signin.html', context)



def signin_empleado(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['email']
			if User.objects.filter(username=username).exists():
				context = {
					'error_message': 'El usuario ya existe',
					'form': form
				}
				return render(request, 'signin_empleado.html', context)
			else:
				password = form.cleaned_data['password1']
				password2 = form.cleaned_data['password2']
				if password != password2:
					context = {
						'error_message': 'Las constraseñas no coinciden',
						'form': form
					}
					return render(request, 'signin_empleado.html', context)
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				new_user = User(username=username, password=password, first_name=first_name, last_name=last_name) 
				new_user.save()
				try:
					group = Group.objects.get(name='empleados')
				except Group.DoesNotExist:
					group = Group(name='empleados')
					group.save()
				new_user.groups.add(group)
				form = RegisterForm()
				context = {
					'success_message': 'Usuario empleado creado correctamente',
					'form': form
				}
				return render(request, 'signin_empleado.html', context)

		else:
			form = RegisterForm()
			context = {
				'error_message': 'La información no es valida, porfavor intente nuevamente',
				'form': form
			}
			return render(request, 'signin_empleado.html', context)
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

def logout(request):
    django_logout(request)
    return redirect('index')

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

def armar_pc(request):
	user = request.user
	# if user.is_authenticated():
	print(user)
	if user.is_staff:
		print('user is staff')
	if user.is_superuser:
		print('user is super user')
	if es_empleado(user):
		print('user is empleado')
	return render(request, 'armar_pc.html')

def nuevo_empleado():
	pass

def nuevo_insumo(request):
	user = request.user
	if not es_empleado(user):
		return redirect('index')

	if request.method == 'POST':
		articulo = ArticleForm(request.POST, request.FILES) 
		if articulo.is_valid():
			articulo.save()
			form = ArticleForm()
			context = {
				'success_message': 'Articulo creado con exito',
				'form': form
			}
			return render(request, 'gestion_nuevo_insumo.html', context)
		else:
			context = {
				'form': articulo
			}
			return render(request, 'gestion_nuevo_insumo.html', context)
	else:
		form = ArticleForm()
		context = {
			'form': form
		}
		return render(request, 'gestion_nuevo_insumo.html', context)
	return render(request, 'gestion_nuevo_insumo.html')

def listar_insumos(request):
	listado_insumos = Articulo.objects.all() # TODO trae imagenes también
	context = {
	'listado_insumos': listado_insumos
	}
	return render(request, 'gestion_listar_insumos.html', context)
	
def modificar_insumo(request, insumo_id):
	insumo = Articulo.objects.get(id=insumo_id)
	# TODO return render del objeto, modificar y eliminar
	return HttpResponse('as')

def es_empleado(user):
    return user.groups.filter(name='empleados').exists()

def es_admin(user):
    return user.groups.filter(name='admin').exists()

def test(request):
	return render(request, 'test.html')

#--------------------- deprecated ---------------------

def signin_empleado2(request):
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