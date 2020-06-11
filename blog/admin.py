from django.contrib import admin
from .models import Post #nós importamos (incluímos) o modelo Post definido no capítulo anterior

admin.site.register(Post) #Para tornar nosso modelo visível na página de administração, precisamos registrá-lo

# Register your models here.
