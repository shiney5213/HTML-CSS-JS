from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')