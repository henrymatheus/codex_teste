from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField("Data de nascimento")
    curso = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula})"
