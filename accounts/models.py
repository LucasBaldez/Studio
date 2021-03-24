from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
