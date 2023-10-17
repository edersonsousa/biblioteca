from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros, Categoria, Emprestimo
# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario)
        return render(request,'home.html', {'livros': livros})

    else:
        return redirect('/auth/login/?status=2')

def ver_livro(request, id):
    if request.session.get('usuario'):    
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id :
            #categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario')) # Torno aqui a categorização colaborativa
            categoria_livro = Categoria.objects.all()
            emprestimos = Emprestimo.objects.filter(livro = livro)
            print(emprestimos)
            return render(request, 'ver_livro.html', {'livro': livro, 'categoria_livro': categoria_livro, 'emprestimos': emprestimos})
        else:
            return redirect('/livro/home')
    return redirect('/auth/login/?status2')