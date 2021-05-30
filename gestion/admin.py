from django.contrib import admin
from .models import *


admin.site.register(Proveedor)
admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(Compra)
admin.site.register(Stock)


# Register your models here.
