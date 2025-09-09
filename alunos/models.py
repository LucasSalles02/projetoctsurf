from django.db import models
from turmas.models import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # depois pode usar hash
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)  # formato 000.000.000-00
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    desempenho = models.TextField(blank=True, null=True)
    frequencia = models.FloatField(default=0)

    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="alunos"
    )

    def __str__(self):
        return self.nome
