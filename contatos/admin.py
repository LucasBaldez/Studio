from django.contrib import admin
from .models import Categoria, Contato, Procedimento
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','categoria','procediemnto','mostrar')


admin.site.register(Categoria)
admin.site.register(Contato)
admin.site.register(Procedimento)

