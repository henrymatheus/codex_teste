# Sistema de Cadastro de Alunos (Django)

Aplicação Django para cadastro, edição, listagem e remoção de alunos.

## Requisitos

- Python 3.10+
- pip

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

## Funcionalidades

- Cadastro de alunos
- Listagem de alunos
- Edição de dados
- Exclusão com confirmação
- Validação de e-mail e matrícula únicos
- Administração pelo Django Admin (`/admin`)
