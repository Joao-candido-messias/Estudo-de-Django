from django.shortcuts import render

def index(request):
    """Página principal do learning Log"""
    return render(request, 'learning_logs/index.html')


