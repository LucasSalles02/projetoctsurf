from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    
    MODALIDADES_CHOICES = (
        ('', '--- Selecione a Modalidade ---'), 
        ('Iniciação', 'Iniciação'),
        ('Formação', 'Formação'),
    )
    
    modalidade = forms.ChoiceField(
        choices=MODALIDADES_CHOICES,
        required=True, 
        label='Modalidade de Ensino',
        widget=forms.Select(attrs={"class": "campo-input"})
    )

    class Meta:
        model = Aluno
        
        fields = [
            "modalidade", 
            "nome",
            "data_nascimento",
            "cpf",
            "endereco",
            "bairro",
            "cidade",
            "cep",
            "nome_responsavel",
            "cpf_responsavel",
            "numero_responsavel",
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "campo-input", "placeholder": "Nome completo"}),
            "data_nascimento": forms.DateInput(attrs={"type": "date", "class": "campo-input"}),
            
           
            "cpf": forms.TextInput(attrs={
                "class": "campo-input", 
                "placeholder": "000.000.000-00",
                "maxlength": "14"
            }),
            
            "endereco": forms.TextInput(attrs={"class": "campo-input", "placeholder": "Rua, número"}),
            "bairro": forms.TextInput(attrs={"class": "campo-input"}),
            "cidade": forms.TextInput(attrs={"class": "campo-input"}),
            "cep": forms.TextInput(attrs={"class": "campo-input", "placeholder": "00000-000"}),
            "nome_responsavel": forms.TextInput(attrs={"class": "campo-input", "placeholder": "Nome completo do responsável"}),
            
           
            "cpf_responsavel": forms.TextInput(attrs={
                "class": "campo-input", 
                "placeholder": "000.000.000-00",
                "maxlength": "14" 
            }),
            
            "numero_responsavel": forms.TextInput(attrs={"class": "campo-input", "placeholder": "(22) 99999-9999"}),
        }