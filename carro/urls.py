# url - view - template
from django.urls import path, reverse_lazy
from .views import HomepageCarro, Homepage, DetalhesCarro, PesquisarCarro, logout_view, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_view


app_name = 'carro'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('Carros/', HomepageCarro.as_view(), name='homepageCarro'),
    path('Carros/<int:pk>', DetalhesCarro.as_view(), name='detalhesCarro'),
    path('Carros/Pesquisa/', PesquisarCarro.as_view(), name='pesquisacarro'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('editar/<int:pk>', PaginaPerfil.as_view(), name='editarperfil'),
    path('CriarConta/', CriarConta.as_view(), name='criarConta'),
    path('mudarsenhar/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('carro:homepageCarro')), name='mudarsenha')
]
