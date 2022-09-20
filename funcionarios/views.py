from django.shortcuts import render
from .models import Perfil, Funcionarios,Departamento

# Views criadas.


# Create your views here.
def listar_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})
