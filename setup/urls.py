from django.contrib import admin
from django.urls import path

from funcionarios.views import FuncionarioListView, FuncionarioCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", FuncionarioListView.as_view(),name="funcionario_list"),
    path("create", FuncionarioCreateView.as_view(),name="funcionario_create"),
]
