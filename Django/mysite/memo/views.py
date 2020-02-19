from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import CharField, Textarea
from . import models
from . import forms
from . import apps

def index(request):
    return HttpResponse('ok')


class MemoView(View):
    def get(self, request, category, pk, mode):
        if mode == 'add':
            form = forms.MemoForm()
        
        elif mode == 'list':
            username = request.session.get('username', '')
            user = User.objects.get(userid = username)

            # user가 쓴 글만 filtering
            data = models.Memo.objects.all().filter(author = user)
            context = {'data': data, 'username': username, 'category': category}
            return render(request, apps.APP +  '/list.html', context)

        elif mode == 'detail':
            #pk = username(id)
            p = get_object_or_404(models.Memo, pk = pk)
            
            # 조회수 증가
            p.cnt +=1
            p.save
            return render(request, apps.APP + 'detail.html', {'d': p, 'category': category})

        elif mode == 'edit':
            post = get_object_or_404(models.Memo, pk = pi)
            form = forms.MemoForm(instance = post)

        else:
            return HttpResponse('mode를 다시 입력하세요')
        return render(request, apps.APP + '/edit.html', {'form': form})

    # post는 입력/수정일 때만 해당
    def post(self, request, category, pk, mode):
        username = request.session['username']
        user = User.objects.get(username = username)

        if pk == 0:
            form = form.MemoForm(request.POST)
        else:
            post = get_object_or_404(models.Memo, pk = pk)
            form = forms.MemoForm(request.POST, instance = post)

        if form.is_valid():
            post = form.save(commit = False)
            if pk == 0:
                post.author = user
            post.save()

            return redirect('Memo', category, 0, 'list')
        return render(request, apps.APP + '/edit.html', {'form': form})


