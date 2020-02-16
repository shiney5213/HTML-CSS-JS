from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from datetime import datetime
# Create your views here.

def index(request):
    return HttpResponse('Hello~~~')


def input(request):
    return render(request, 'birthday/input.html')

def output(request):
    send = request.GET['send']
    msg = request.GET['msg']
    name = request.GET['name']
    year = request.GET['year']
    month = request.GET['month']
    day = request.GET['day']
    today = datetime.now()
    cur_year = today.year-int(year) + 1

    data = '사랑하는 ' + name + '에게<br>' +month+'월' +day+'일 생일을<br> 진심으로 축하해!<br>' + msg + '<br><br>' + str(cur_year) +'번째 생일을 축하하며<br>' + send + '가'
    

    return HttpResponse(data)

