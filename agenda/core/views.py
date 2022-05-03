from django.shortcuts import render

def lista_eventos(request):
    return render(request, 'agenda.html')