from audioop import reverse
from email import message
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.views import generic

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, page_role_controller
from django.urls import reverse_lazy

# Create your views here.
from .models import *
from .forms import CreateUserForm, UpdateUserForm, UpdateProfileForm


def inicio(request):
    return render(request, 'inicial.html')

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cliente_home')
        else:
            messages.warning(request, 'Utilizador ou Password incorreto')
            

    context = {}
    return render(request, 'login.html', context)

@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                
                group = Group.objects.get(name='client')
                user.groups.add(group)

                messages.success(request, 'Conta criada com sucesso')

                return redirect('login')

        context = {'form': form}
        return render(request, 'registar.html', context)

def logoutUtilizador(request):
    logout(request)
    return redirect('home')

#PT
@login_required(login_url='login')
@allowed_users(allowed_roles=['pt'])
def ptInicial(request):
    return render(request, 'pt_inicial.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['pt'])
def pt_perfil(request):
    return render(request, 'pt_perfil.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['pt'])
def pt_perfil_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil atualizado')
            return redirect('pt_perfil')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'pt_perfil_update.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['pt'])
def pt_perfil(request):
    return render(request, 'pt_perfil.html')

#Cliente
@login_required(login_url='login')
@page_role_controller
def clienteInicial(request):
    return render(request, 'cliente_inicial.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_treino(request):
    return render(request, 'cliente_treino.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_dieta(request):
    return render(request, 'cliente_dieta.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_pt(request):
    return render(request, 'cliente_pt.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_aulas(request):
    return render(request, 'cliente_aulas.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_perfil_update(request):

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil atualizado')
            return redirect('cliente_perfil')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'cliente_perfil_update.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def cliente_perfil(request):
    return render(request, 'cliente_perfil.html')
####

#Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def adminInicial(request):
    return render(request, 'admin_inicial.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_procurarcliente(request):

    displayclients=User.objects.all()

    return render(request, 'admin_procurarcliente.html',{"displayclients":displayclients})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_aulas(request):
    return render(request, 'admin_aulas.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pt(request):
    return render(request, 'admin_pt.html')
####



