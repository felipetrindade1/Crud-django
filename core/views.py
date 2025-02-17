from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    nome = request.POST.get('nome')
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):

    pessoas = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoas": pessoas})

def update(request, id):
    vnome = request.POST.get('nome')
    pessoas = Pessoa.objects.get(id=id)
    pessoas.nome = vnome
    pessoas.save()
    

    return redirect(home)

def delete(request, id):
    pessoas = Pessoa.objects.get(id=id)
    pessoas.delete()
    
    return redirect(home)