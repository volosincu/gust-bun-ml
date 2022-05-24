from django.shortcuts import render


def index(request):
    """HOME PAGE"""
    return render(request, 'index.html')
