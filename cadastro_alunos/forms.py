from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "email", "matricula", "data_nascimento", "curso", "ativo"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
        }
