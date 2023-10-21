from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CategoriaLivro


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario)
        form = CadastroLivro()
        status_categoria = request.GET.get('cadastro_categoria')
        form.fields['usuario'].initial = request.session['usuario']
        #Para trazer apenas as categoria cadastradas pelo usuário
        #Acho válido repensar isso depois
        form_categoria = CategoriaLivro()
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario= usuario)

        return render(request,'home.html', {'livros': livros, 
                                            'usuario_logado': request.session.get('usuario'),
                                            'form': form,
                                            'status_categoria': status_categoria,
                                            'form_categoria':form_categoria
                                             })

    else:
        return redirect('/auth/login/?status=2')

def ver_livro(request, id):
    if request.session.get('usuario'):    
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id :
            #categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario')) # Torno aqui a categorização colaborativa
            categoria_livro = Categoria.objects.all()
            usuario = Usuario.objects.get(id = request.session['usuario'])
            emprestimos = Emprestimo.objects.filter(livro = livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            #Para trazer apenas as categoria cadastradas pelo usuário
            #Acho válido repensar isso depois
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario= usuario)
            form_categoria = CategoriaLivro()
            
            return render(request, 'ver_livro.html', {  'livro': livro, 
                                                        'categoria_livro': categoria_livro, 
                                                        'emprestimos': emprestimos, 
                                                        'usuario_logado': request.session.get('usuario'),
                                                        'form': form,
                                                        'id_livro': id,
                                                        'form_categoria':form_categoria
                                                    })
        else:
            return redirect('/livro/home')
    return redirect('/auth/login/?status2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('Dados Inválidos')

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id = id_usuario)
        categoria = Categoria(nome = nome, descricao = descricao, usuario = user)
        categoria.save()
        return redirect('/livro/home?cadastro_categoria=1')
    else:
        return HttpResponse('Errooooo')
