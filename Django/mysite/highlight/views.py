from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips
import cv2
import os
from . import apps
import shutil, time
# from .dataAnalysis import preprocessing
# from .dataAnalysis import modelpredict
# from .dataAnalysis import isgame_test
# from .dataAnalysis import usingdata
from .dataAnalysis import audio2text
from .dataAnalysis import cropVideo, makeVideo




# Create your views here.
global sub_index, filename, base_root, pluscount, dirname, args, audio_file

# filename = 'test30m.mp4'
# pluscount  = 18000
# filename = 'test.mp4'
pluscount = 1000
# filename = 'test10m.mp4'
# pluscount = 10000
job_name = 'hi_6'
filename = 'test_title.mp4'


dirname = filename.replace('.mp4', '')
base_root = settings.BASE_DIR + f"/static/highlight/{dirname}/"
audio_file = filename.replace('mp4', 'mp3')


args = {
        'filename': filename,
        'crop_filename': f'{dirname}_2.mp4',
        'final_filename': f'{dirname}_final.mp4',
        'pluscount': pluscount,
        'dirname': dirname,
        'base_root': base_root,
        'audio_file': filename.replace('mp4', 'mp3'),
        'crop_audio': f'{dirname}_2.mp3',
        'image_root': base_root + 'image/',
        'data_root': base_root + 'data/',
        'video_root': base_root + 'video/',
        'audio_root': base_root + 'audio/',
        
        #asw
        'AWS_ACCESS_KEY_ID':  'AKIAS3UCLIDDHDXHMWOZ',
        'AWS_SECRET_ACCESS_KEY' : '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',
        'AWS_DEFAULT_REGION' : 'ap-northeast-2',
        'region' : 'ap-northeast-2',
        'bucket' : 'eyshin',
        #transcript
        'font_setting' :'MDotum', 
        'job_name': job_name,
        'LanguageCODE': 'ko-KR',
        'subtitles_file' : f'{dirname}.srt',
        'subtitles_file2' : f'{dirname}_2.srt',
    }



class highlightView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(highlightView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'highlight/highlight.html')


    def post(self, request):
        # print(request.POST.keys())
        datapath =  './static/highlight/substitle.txt'
        # print(os.path.isfile(datapath))

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
        global sub_index

        # video crop
        # save_start = request.POST.get('save_start', '')
        # save_end =request.POST.get('save_end', '')
        # crop_filename = cropVideo.crop(args,save_start, save_end)
        # print(crop_filename, 'success')

    
        # s3 -> transcribe
        sub_index, sub_time, sub_text = audio2text.startSTT( args, args['crop_filename'])
    
        print(len(sub_index), len(sub_time), len(sub_text) )

        context = {'crop_file': args['crop_filename'],
                    'sub_index': sub_index,
                    'sub_time': sub_time,
                    'sub_text': sub_text,
                    }   

        return render(request, 'highlight/subtitle.html', context)


class makesubtitleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(makesubtitleView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'highlight/last.html')

    def post(self, request):
        global sub_index

        dict_keys = request.POST.keys()
        print('dict-keys', dict_keys)
        
        index_dict = {}
        time_dict = {}
        text_dict = {}

        for dict_key in dict_keys:
            if 'indexBtn' in dict_key:
                key = int(dict_key.replace('indexBtn',''))+(1)
                index_dict[key]=request.POST.get(dict_key)
            if 'timeInput' in dict_key:
                key = int(dict_key.replace('timeInput',''))+ 1
                time_dict[key]=request.POST.get(dict_key)
            if 'textInput' in dict_key:
                key = int(dict_key.replace('textInput',''))+1
                text_dict[key]=request.POST.get(dict_key)


        make_result = makeVideo.saveSrt(args, index_dict,time_dict,text_dict)
        print('make', make_result)

        final_result =makeVideo.mergeVideo(args)
        if final_result:
            return render(request, 'highlight/last.html')


    



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

