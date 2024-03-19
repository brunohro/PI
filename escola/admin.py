from django.contrib import admin
from .models import Professor, Disciplina, Aluno, Cidade

admin.site.register(Cidade)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
