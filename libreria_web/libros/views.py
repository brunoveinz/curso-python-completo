from django.shortcuts import render
from .models import Libro, Categoria
from django.db.models import Count

# Create your views here.
def vista_principal(request):
    return render(request, 'index.html')

def vista_libros(request):

    libros = Libro.objects.all()

    context = {
        'libros' : libros
    }

    return render(request, 'libros.html', context)

def vista_categorias(request):

    categorias = Categoria.objects.annotate(
        total_libros = Count('libros')
    )


    context = {
        'categorias' : categorias,
        'total_libros' : categorias.count()        
    }

    return render(request, 'categorias.html', context)