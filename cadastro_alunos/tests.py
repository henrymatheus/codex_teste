from django.test import TestCase
from django.urls import reverse

from .models import Aluno


class AlunoViewsTests(TestCase):
    def test_lista_alunos_disponivel(self):
        response = self.client.get(reverse("lista_alunos"))
        self.assertEqual(response.status_code, 200)

    def test_cria_aluno_com_sucesso(self):
        payload = {
            "nome": "Maria Silva",
            "email": "maria@escola.com",
            "matricula": "2024001",
            "data_nascimento": "2005-03-10",
            "curso": "Matemática",
            "ativo": True,
        }
        response = self.client.post(reverse("criar_aluno"), data=payload)
        self.assertRedirects(response, reverse("lista_alunos"))
        self.assertTrue(Aluno.objects.filter(email="maria@escola.com").exists())
