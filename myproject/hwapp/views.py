from django.shortcuts import render


def index(request):
    return render(request, 'hwapp/index.html')


def about(request):
    return render(request, 'hwapp/about.html')
