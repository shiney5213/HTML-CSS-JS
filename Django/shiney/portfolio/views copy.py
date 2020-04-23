from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
import os
from .deepmoticon import main
import imutils 


########## 테스트 함수
# def index(request):
# 	return /HttpResponse('portfolio 보자!')

# def deepmoticonForm(request):
#     return HttpResponse('portfolio 보자')

# def deepmoticon(request):
#     return render(request, 'portfolio/deepmoticon/port_main.html')


########## 포트폴리오 메인 페이지
class portfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/port_main.html')


########## deepmoticon 

class UploadView(View):
    def get(self, request):
        return render(request, 'portfolio/deepmoticon/image_upload.html')

    def post(self, request):

        try: 
            file = request.FILES.get('filename', '')
            filename = file._name
            
            
            if file == '':
                return HttpResponse('file을 다시 upload해주세요')
            else:
                fp = open(settings.BASE_DIR + f'/static/portfolio/deepmoticon/{filename}' , 'wb')
                for chunk in file.chunks():
                    fp.write(chunk)
                fp.close()

        except:
            filename = request.POST['filename']

        ##### 이모티콘 만들기
        main.deepmoticon_start(filename)  


        ##### 이모티콘 mp4가져오기
        dirname = filename.replace('jpg','').replace('png','').replace('.','')
        output_dir = settings.BASE_DIR + f'/static/portfolio/deepmoticon/{dirname}'
        output_list = os.listdir(output_dir)
        print(len(output_list))
        
        video_files = []
        for video_file in output_list:
            if 'mp4' in video_file:
                video_files.append(video_file)

        video_list1 = []
        video_list2 = []
        for files in video_files:
            if len(video_list1) < int(len(video_files)/2):
                video_list1.append(f'{dirname}/{files}')
            else:
                video_list2.append(f'{dirname}/{files}')

         
        context= {'data': filename, 'video_files1': video_list1, 'video_files2': video_list2}

        # return HttpResponse('file upload success')
        return render(request, 'portfolio/deepmoticon/image_result.html', context)


