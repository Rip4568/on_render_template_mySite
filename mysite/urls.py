from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #rotas para a configuração de administração
    path('admin/', admin.site.urls),
    #rotas para o aplicativo
    path('',include('render.urls')),
    #rotas para as dependencias
    path('unicorn/',include('django_unicorn.urls'))
]