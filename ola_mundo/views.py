from django.http import HttpResponse
from django.shortcuts import render


def ola_mundo(request):

    #return HttpResponse("Ola mundo")
    texto = "Olá Mundo!!!!!" * 2
    return render(request, "ola_mundo.html", {"texto": texto})
