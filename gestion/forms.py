from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import MultiWidget, TextInput, PasswordInput
from .models import Articulo
from django.forms import ModelForm

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
	
class ArticleForm(ModelForm):
	class Meta:
		model = Articulo
		fields = ['nombre', 'precio','marca', 'categoria', 'imagen']
		widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'custom-select'}),
            'categoria': forms.Select(attrs={'class': 'custom-select'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }
        









###########################################################################################
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

# ejemplo de model form
# from django.utils.translation import gettext_lazy as _

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         labels = {
#             'name': _('Writer'),
#         }
#         help_texts = {
#             'name': _('Some useful help text.'),
#         }
#         error_messages = {
#             'name': {
#                 'max_length': _("This writer's name is too long."),
#             },
#         }