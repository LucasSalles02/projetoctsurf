from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "idade", "cpf", "turma", "frequencia")
    search_fields = ("nome", "email", "cpf")
    list_filter = ("turma", "idade")
