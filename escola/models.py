from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

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
