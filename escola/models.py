from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    celular = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
