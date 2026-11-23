from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST
from nomina.forms import RegistroForm


def registro_view(request):
    if request.user.is_authenticated:
        return redirect('rol_list')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_consultores, _ = Group.objects.get_or_create(name='consultores')
            user.groups.add(grupo_consultores)
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}. Tu cuenta fue creada en el grupo Consultores.')
            return redirect('rol_list')
    else:
        form = RegistroForm()
    return render(request, 'nomina/auth/registro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('rol_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Sesión iniciada como {user.username}.')
            siguiente = request.GET.get('next') or 'rol_list'
            return redirect(siguiente)
    else:
        form = AuthenticationForm()
    return render(request, 'nomina/auth/login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')