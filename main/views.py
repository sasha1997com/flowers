from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def bouquets(request):
    return render(request, 'main/bouquets.html')
