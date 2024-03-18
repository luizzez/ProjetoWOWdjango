from django.contrib import admin
from .models import Carro
from .models import Usuario
from django .contrib.auth.admin import UserAdmin


admin.site.register(Carro)
admin.site.register(Usuario, UserAdmin)
