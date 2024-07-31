from django.forms import ModelForm
from app.models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa 
        fields = ['Cpf', 'NomeCompleto', 'Email', 'Telefone_celular']