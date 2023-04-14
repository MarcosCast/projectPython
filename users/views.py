'''from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    if request.method == "GET":
       return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get(from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # TODO: Validar força da senha, retornar depois para ajustar

        if not (senha == confirmar_senha):    
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/users/cadastro')   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        #user.save()
        # return redirect(reverse('login'))
        return HttpResponse('Teste'))'''


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # TODO: Validar força da senha, retornar depois para ajustar

        if not (senha == confirmar_senha):    
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/users/cadastro')   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        #user.save()
        # return redirect(reverse('login'))
        return HttpResponse('Teste')
