from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import sys
from io import StringIO
# from jupyter.models import User
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return HttpResponse('jupyter notebook~~~')


def input(request):
    return render(request, 'jupyter/notebook.html')


glo = {}
loc = {}
def output(request):
    code = request.GET.get('code','')

    original_stdout = sys.stdout
    sys.stdout = StringIO()
    exec(code, glo, loc)
    contents = sys.stdout.getvalue()
    sys.stdout = original_stdout
    contents = contents.replace('/n', '<br>')
    contents = '<font color = red>result</font><br>' + contents

    return HttpResponse(contents)


def listuser(request):
    data = User.objects.all()
    return render(request, 'jupyter/database.html', {'data': data})
