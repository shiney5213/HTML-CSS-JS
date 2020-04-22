from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View


# Create your views here.
def index(request):
	#return HttpResponse('deepmoticon 보자!')
    return render(request, 'deepmoticon/port_main.html')

def deepmoticonMain(request):
    return JsonResponse('result': 성공하자!)

# class deepmoticonView(View):
#     def get(self, request):
#         return render(request, 'deepmoticon/port_main.html')