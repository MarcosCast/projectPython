from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required

# Create your views here.
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')