from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import MultiWidget, TextInput, PasswordInput


class LoginForm(forms.Form):
	username = forms.CharField(max_length=16)
	password = forms.CharField(max_length=16)

# nuevo register form sin workaroud
class RegisterForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'text-center'}))
	password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'minlength': '8', 'autocomplete': 'new-password', 'class': 'text-center'}))
	password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'minlength': '8', 'autocomplete': 'new-password', 'class': 'text-center'}))
	first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'minlength': '3', 'class': 'text-center'}))
	last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'minlength': '3', 'class': 'text-center'}))
	







# vieja forma
class RegisterForm2(UserCreationForm):
	# Workaround problem:
	# The Meta.widgets option doesn't apply to fields that were declared in the form. See the note in the docs. In this case, password1 and password2 are declare on the UserCreationForm (they aren't model fields), therefore you can't use them in widgets
	password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
		'placeholder': 'contraseña', 'readonly': 'true',
		'onfocus': 'this.removeAttribute("readonly")',
		'class': 'text-center',
		# 'class': 'form-control'
		}))
	password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
		'placeholder': 'confirmar contraseña',
		'class': 'text-center',
		}))

	class Meta:
		model = User
		fields = ("username", "password1", "password2", 'first_name', 'last_name')
		widgets = {	        
        	'username': TextInput(attrs = {
	        	'placeholder': 'usuario',
	        	'data-validation': 'custom',
	        	'class': 'text-center',
	        }),
	        'first_name': TextInput(attrs = {
	        	'placeholder': 'nombre',
	        	'data-validation': 'custom',
	        	'class': 'text-center',
	        }),
	        'last_name': TextInput(attrs = {
	        	'placeholder': 'apellido',
	        	'data-validation': 'custom',
	        	'class': 'text-center',
	        }),
        }

    # Para remover el autofocus que genera django
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.pop("autofocus", None)