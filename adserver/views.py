from django.shortcuts import render


def index(request):
    return render(request, 'adserver/index.html')
