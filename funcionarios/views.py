from django.shortcuts import render
from .models import Funcionario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
# def funcionarios_list(request):
#     funcionarios = Funcionario.objects.all
#     return render(request,"funcionarios/funcionarios_list.html",{"funcionarios": funcionarios})

class FuncionarioListView(ListView):
    model = Funcionario
    
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = [ "nome" , "sobrenome" , "data_de_nascimento" , "cargo" , "salario" ]
    success_url =reverse_lazy("funcionario_list")
