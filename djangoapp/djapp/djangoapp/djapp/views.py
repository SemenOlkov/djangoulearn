from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')


def usability(request):
    return render(request, 'usability.html')


def cities(request):
    return render(request, 'cities.html')


def skills(request):
    return render(request, 'skills.html')


def last_vacs(request):

    return render(request, 'last_vacs.html')