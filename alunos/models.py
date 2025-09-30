from django.db import models

class Aluno(models.Model):
    # Campos PRINCIPAIS
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=200)
    
    # Campos de Endereço
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)

    # Campos de Responsável
    nome_responsavel = models.CharField(max_length=100)
    cpf_responsavel = models.CharField(max_length=11)
    numero_responsavel = models.CharField(max_length=11)


    def __str__(self):
        return self.nome