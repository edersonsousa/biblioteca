from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros
# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario)
        return render(request,'home.html', {'livros': livros})

    else:
        return redirect('/auth/login/?status=2')

def ver_livro(request, id):
    livro = Livros.objects.get(id = id)
    return render(request, 'ver_livro.html', {'livro': livro})