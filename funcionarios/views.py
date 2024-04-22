from django.shortcuts import render
from .models import Funcionario

# Create your views here.
def funcionarios_list(request):
    funcionarios = Funcionario.objects.all
    return render(request,"funcionarios/funcionarios_list.html",{"funcionarios": funcionarios})
    