from django.shortcuts import redirect, render
from catalogo.form.libro_form import LibroForm
from catalogo.models.libro import Libro   


def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 
                'catalogo/libros/libro_list.html', 
                {'libros': libros})

def libro_create(request):
    if request.method == 'POST': 
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 
                'catalogo/libros/libro_form.html', 
                {'form': form})

def libro_update(request, pk):  
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 
                'catalogo/libros/libro_form.html', 
                {'form': form})

def libro_delete(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 
                'catalogo/libros/libro_confirm_delete.html', 
                {'libro': libro})