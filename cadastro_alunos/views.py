from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm
from .models import Aluno


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos/lista.html", {"alunos": alunos})


def criar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno cadastrado com sucesso!")
            return redirect("lista_alunos")
    else:
        form = AlunoForm()
    return render(request, "alunos/form.html", {"form": form, "titulo": "Cadastrar aluno"})


def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno atualizado com sucesso!")
            return redirect("lista_alunos")
    else:
        form = AlunoForm(instance=aluno)
    return render(request, "alunos/form.html", {"form": form, "titulo": "Editar aluno"})


def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        aluno.delete()
        messages.success(request, "Aluno removido com sucesso!")
        return redirect("lista_alunos")
    return render(request, "alunos/confirmar_exclusao.html", {"aluno": aluno})
