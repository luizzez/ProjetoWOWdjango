from .models import Carro

def lista_mais_acessados(request):
    lista_carros = Carro.objects.all().order_by('-curtidas')[0:3]
    return {"lista_mais_acessados": lista_carros}