from django.contrib import admin
from django.urls import path

from funcionarios.views import funcionarios_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", funcionarios_list)
]
