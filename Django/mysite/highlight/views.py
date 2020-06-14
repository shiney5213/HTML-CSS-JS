from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# from moviepy.editor import VideoFileClip, concatenate_videoclips
import cv2
import os

# Create your views here.

class highlightView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(highlightView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'highlight/highlight.html')


    def post(self, request):
        print(request.POST.keys())
        datapath =  './static/highlight/substitle.txt'
        print(os.path.isfile(datapath))

        with open(datapath, 'r', encoding ='UTF-8' ) as f:
            datas=f.read()
        
        datas = datas.replace("'", '')
        datas = datas.split('\\n\\n')
        sub1 = []
        for data in datas:
            if data !='' :
                sub1.append(data.split('\\n'))
        sub2 =[]
        for sub in  sub1:
            timedata =sub[1][:8]+'-->'+sub[1][18:26]
            # print(timedata)
            sub2.append([sub[0], timedata, sub[2]])

        # save_path = settings.BASE_DIR +'/static/highlight/subtitle_final.txt'
        # with open(save_path, 'w', encoding = 'UTF-8') as f:
        #     f.write(str(sub2))    
        print('sub2', sub2)
        context = {'subtitle': sub2}    
        return redirect('/highlight/subtitle', context)
        # return render(request, 'highlight/subtitle.html', context)

class subtitleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(subtitleView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'highlight/subtitle.html')


    def post(self, request):
        print(request.POST.keys())
        datapath =  './static/highlight/substitle.txt'
        print(os.path.isfile(datapath))

        with open(datapath, 'r', encoding ='UTF-8' ) as f:
            datas=f.read()
        
        datas = datas.replace("'", '')
        datas = datas.split('\\n\\n')
        sub1 = []
        for data in datas:
            if data !='' :
                sub1.append(data.split('\\n'))
        sub2 =[]
        for sub in  sub1:
            timedata =sub[1][:8]+'-->'+sub[1][18:26]
            # print(timedata)
            sub2.append([sub[0], timedata, sub[2]])

        # save_path = settings.BASE_DIR +'/static/highlight/subtitle_final.txt'
        # with open(save_path, 'w', encoding = 'UTF-8') as f:
        #     f.write(str(sub2))    
        # print('sub2', sub2)
        sub_length= []
        sub_time = []
        sub_text = []
        sub_dict = {}
        for (i, time, text) in sub2:
            time2 = time.replace(',','').replace(' ','').replace(':', ';')
            i = i.replace(' ', '')
            text = text.replace(' ', '')
            sub_length.append(i)
            sub_time.append(time2)
            sub_text.append(text)
            sub_dict[i]=[sub_time, sub_text]

        
        print(len(sub_length), len(sub_time), len(sub_text) )

        context = {'sub_length': sub_length,
                'sub_time': sub_time,
                'sub_text': sub_text,
                'sub_dict': sub_dict,
                }   


        return render(request, 'highlight/subtitle.html', context)





# def index(request):
#     # return HttpResponse('Hello~~~')
#     return render(request, 'highlight/highlight.html')


# @csrf_exempt
# def subtitle(request):
#     print(request.GET.keys())
#     datapath =  './static/highlight/substitle.txt'
#     print(os.path.isfile(datapath))

#     with open(datapath, 'r', encoding ='UTF-8' ) as f:
#         datas=f.read()
    
#     datas = datas.replace("'", '')
#     datas = datas.split('\\n\\n')
#     sub1 = []
#     for data in datas:
#         if data !='' :
#             sub1.append(data.split('\\n'))
#     sub2 =[]
#     for sub in  sub1:
#         timedata =sub[1][:8]+'-->'+sub[1][18:26]
#         # print(timedata)
#         sub2.append([sub[0], timedata, sub[2]])

#     # save_path = settings.BASE_DIR +'/static/highlight/subtitle_final.txt'
#     # with open(save_path, 'w', encoding = 'UTF-8') as f:
#     #     f.write(str(sub2))    

#     context = {'subtitle': sub2}    

    # return render(request, 'highlight/subtitle.html', context )

