from django.contrib import admin
from .models import Servico, Cargo, Funcionario


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo', 'criado')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criado')
