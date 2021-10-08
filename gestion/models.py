from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Proveedor(models.Model):
	nombre = models.CharField(max_length=30)
	correo = models.EmailField(max_length=254, blank=True)
	telefono = models.IntegerField(validators=[MinValueValidator(0)])

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.nombre

class Marca(models.Model):
	nombre = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.nombre

		
# ImageField necesita install Pillow por pip
class Articulo(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True) 
    imagen = models.ImageField(upload_to='imagenes/articulos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, models.SET_NULL, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.SET_NULL, blank=True, null=True)

    def __str__(self):
    	return self.nombre

class Venta(models.Model):
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	monto = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateField(auto_now=False, auto_now_add=True)
	usuario = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.nombre

class DetalleVenta(models.Model):
	articulo = models.ForeignKey(Articulo, models.SET_NULL, blank=True, null=True)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.articulo.nombre + str(self.cantidad) + str(self.precio)

class Compra(models.Model):
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateField(auto_now=False, auto_now_add=True)
	# factura = 

	def __str__(self):
		return str(self.total) + self.fecha

class DetalleCompra(models.Model):
	articulo = models.ForeignKey(Articulo, models.SET_NULL, blank=True, null=True)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

	def __str__(self):
		return self.articulo.nombre + str(self.cantidad) + str(self.precio)

class Stock(models.Model):
	articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])

	def __str__(self):
		return self.articulo.nombre + str(self.cantidad)
