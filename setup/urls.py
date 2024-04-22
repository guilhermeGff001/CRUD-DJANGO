from django.contrib import admin
from django.urls import path

from funcionarios.views import FuncionarioListView, FuncionarioCreateView,FuncionarioUpdateView,FuncionarioDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", FuncionarioListView.as_view(),name="funcionario_list"),
    path("create", FuncionarioCreateView.as_view(),name="funcionario_create"),
    path("update/<int:pk>",FuncionarioUpdateView.as_view(),name="funcionario_update"),
    path("delete/<int:pk>",FuncionarioDeleteView.as_view(),name="funcionario_delete"),
]
