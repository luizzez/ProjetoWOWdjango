from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Carro(models.Model):
    nome = models.CharField(max_length=25)
    imagemCarro = models.ImageField(upload_to='foto_carro')
    descricao = models.TextField(max_length=1000, default="")
    curtidas = models.IntegerField(default=0)
    data_fabricacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    pass