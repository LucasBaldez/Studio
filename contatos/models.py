from django.db import models


class Procedimento(models.Model):
    descricao = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1, default='S')

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1,default='S')

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    procedimento = models.ManyToManyField(Procedimento)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')

    def __str__(self):
        return self.nome

