from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Aluno
from .forms import AlunoForm
# As importações de 'Turma' e 'get_object_or_404' foram removidas.


def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('id') 

    contexto = {
        'alunos': alunos,
        'titulo': 'Lista de Inscrições'
    }
    
    return render(request, 'alunos/lista_alunos.html', contexto)


def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        
        if form.is_valid():
            
            # A modalidade é lida, mas não é usada para buscar a Turma
            modalidade_escolhida = form.cleaned_data.get('modalidade') 
            
            aluno = form.save(commit=False)
            
            # Limpeza dos Campos MASCARADOS (mantida por ser crucial para max_length=11)
            if aluno.cpf:
                aluno.cpf = aluno.cpf.replace('.', '').replace('-', '')
            if aluno.cpf_responsavel:
                aluno.cpf_responsavel = aluno.cpf_responsavel.replace('.', '').replace('-', '')
            
            # TODA A LÓGICA DE BUSCA, TRY/EXCEPT E ATRIBUIÇÃO DA TURMA FOI REMOVIDA.
            
            aluno.save()
            
            return redirect(reverse('alunos:lista_alunos')) 
            
    else:
        form = AlunoForm()

    contexto = {
        'form': form,
        'titulo': 'Nova Inscrição de Aluno'
    }
    
    return render(request, 'alunos/cadastro_aluno.html', contexto)