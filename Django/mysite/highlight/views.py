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
from .dataAnalysis import preprocessing
from .dataAnalysis import modelpredict
from .dataAnalysis import isgame_test
from .dataAnalysis import usingdata
from .dataAnalysis import audio2text
from .dataAnalysis import cropVideo, makeVideo, output
import datetime, random



# Create your views here.
global flag, sub_time, filename, base_root, pluscount, dirname, args, audio_file

job_name = 'hi_40'
flag = 'test'
# flag = 'real'



# filename = 'test30m.mp4'
# pluscount  = 18000

# filename = 'test10m.mp4'
# pluscount = 10000
# filename = 'test30m.mp4'
# pluscount = 180000

# filename = 'test3h.mp4'
# pluscount = 18000
filename = 'test.mp4'
pluscount = 1000



dirname = filename.replace('.mp4', '')

if flag == 'test':
    crop_filename = filename 
    audio_file = crop_filename.replace('mp4', 'mp3')
else:
    crop_filename = f'{dirname}_2.mp4'
    audio_file = crop_filename.replace('mp4', 'mp3')


base_root = settings.BASE_DIR + f"/static/highlight/{dirname}/"
base_root =str(base_root).replace('\\', '/')
audio_file = filename.replace('mp4', 'mp3')


args = {
        'flag': flag,
        'filename': filename,
        'crop_filename': crop_filename,
        
        'final_filename': f'{dirname}_final.mp4',
        'pluscount': pluscount,
        'dirname': dirname,
        'base_root': base_root,
        'audio_file': audio_file,
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


@csrf_exempt
def analysis(request):
    global filename

    # filename = 'test.mp4'
    print('key',request.POST.keys())
    analysis_start = request.POST.get('analysis_start', '0')
    analysis_end =request.POST.get('analysis_end', '1')
 

    print('시간 확인',analysis_start, analysis_end)
    analysis_time = int(float(analysis_end)-float(analysis_start))

    analysisstart = int(float(analysis_start))
    analysisstarttime = str(datetime.timedelta(seconds=analysisstart))
    analysisend = int(float(analysis_end))
    analysisendtime = str(datetime.timedelta(seconds=analysisend))
    print('시간 ', analysisstarttime, analysisendtime)


    #  search highlgith 
    if args['flag'] =='test':
        highlight_rate = [random.random() for i in range(int(analysis_time))]
        d_data = [random.random() for i in range(int(analysis_time))]
        k_data = [random.random() for i in range(int(analysis_time))]
        a_data = [random.random() for i in range(int(analysis_time))]
    else: 
        ddf = preprocessing.main(args, analysisstarttime, analysisendtime)
        # result = modelpredict.modelpre( args, ddf)
        # rate_list = result['probability'].tolist()
        # highlight_rate = [0]*(20+int(float(analysis_start))) + rate_list
        # all, k_data, d_data, a_data = usingdata.delta(args, ddf)
        # k_data = k_data.tolist()
        # d_data = d_data.tolist()
        # a_data = a_data.tolist()
        highlight_rate, k_data, d_data, a_data = output.output(args, ddf)


    color = ['rgba(75, 192, 192, 1)' for i in range (len(highlight_rate))]


    time_data2 = []
    print(analysis_start, analysis_end)
    for i in range(int(analysis_start), int(float(analysis_end))):
        time_data2.append(i)

    context = {'time_data2': time_data2,
                'highlight_rate': highlight_rate,
                'k_data': k_data,
                'a_data': a_data,
                'd_data': d_data,
                'color': color}
    return JsonResponse(context)




class highlightView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(highlightView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # return render(request, 'highlight/hilight_index.html')
        return render(request, 'highlight/highlight_index2.html')


    def post(self, request):
        #video save
        upload_form = UploadFileForm(request.POST)
        print('upload_form', upload_form)

        try: 
            file = request.FILES.get('filename', '')
            filename = file._name
            print('filename',filename)
            
            if file == '':
                return HttpResponse('file을 다시 upload해주세요')
            else:

                # 폴더 만들기
                make_dir = filename.replace('.mp4', '')
                
                video_root =f"./static/highlighteditor/{make_dir}/video/" 
               
                try:
                    os.makedirs(f'./static/highlighteditor/{make_dir}')
                except Exception as err:
                    print(err)
                try:
                    os.makedirs(video_root)
                except Exception as err:
                    print(err)
               

                fp = open(settings.BASE_DIR + f'/static/highlighteditor/{make_dir}/video/{filename}' , 'wb')
                for chunk in file.chunks():
                    fp.write(chunk)
                fp.close()

                fp = open(settings.BASE_DIR + f'/static/highlighteditor/save/{filename}' , 'wb')
                for chunk in file.chunks():
                    fp.write(chunk)
                fp.close()

        except:
            filename = request.POST['filename']
        # context= {'filename': filename, 'dirname': make_dir}
        context= {'data': filename}
        time.sleep(1)
        
        return redirect('', context)
        
@csrf_exempt
def savevideo(request):
    global filename
    print('key',request.POST.keys())

    save_start = request.POST.get('save_start', '')
    save_end =request.POST.get('save_end', '')
    
    print('start', save_start)
    print('end', save_end)

    # crop video
    print('flag', args['flag'])
    if args['flag'] != 'test':
        old_path = args['video_root'] + args['filename']
        new_path = args['video_root'] + args['crop_filename']

        clip = VideoFileClip(old_path).subclip(float(save_start), float(save_end))
        clip.write_videofile(new_path)

    context = {'data': args['crop_filename']
         }
    return  JsonResponse(context)


@csrf_exempt
def startSearch(request):
    global filename, data_path, pluscount
    print('key',request.POST.keys())

    search_start = request.POST.get('search_start', '')
    search_end =request.POST.get('search_end', '')
    
    print('start', search_start)
    print('end',search_end)

    search_start = int(float(search_start))
    search_end = int(float(search_end))

    # search game
    if args['flag'] =='test':
        search_list = []
        for i in range(search_end):
            if i < int(int(search_end)/2):
                search_list.append(1)
            else:
                search_list.append(1)
        time.sleep(1)
    else:
        df = isgame_test.startgame(args)
        print('len', len(df))
        search_list = df[0].tolist()
        
    def lenresize(search_list, window_size):
        res = []
        # window_size = 60
        n = len(search_list)//window_size
        for i in range(n):
            qqq=list(set(search_list[i*window_size:(i+1)*window_size]))
            # print(qqq)

            if len(qqq)==1:
                res.append(qqq[0])
            else :
                res.append(1)
        return res
        
    search_list = lenresize(search_list, 60)
        

    color = ['rgba(75, 192, 192, 1)' for i in range (len(search_list))]
    time_data = [i for i in range(search_start, search_end)]

    context = {'time_data': time_data,
                'search_list': search_list,
                'color': color
                }

    return  JsonResponse(context)


class subtitleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(subtitleView, self).dispatch(*args, **kwargs)

    def get(self, request):
        print('subtitle', request.GET.keys())
        return render(request, 'highlight/subtitle.html')

    def post(self, request):
        global sub_time

        post_key = request.POST.keys()
        print('post_key', post_key)

        if 'save_start' in post_key: 
            # video crop
            save_start = request.POST.get('save_start', '')
            save_end =request.POST.get('save_end', '')
            
            if args['flag'] !='test':
                crop_filename = cropVideo.crop(args,save_start, save_end)
                print(crop_filename, 'success')

            # s3 -> transcribe
            sub_index, sub_time, sub_text = audio2text.startSTT( args, args['crop_filename'])
        
            print(len(sub_index), len(sub_time), len(sub_text) )

            context = {'crop_file': args['crop_filename'],
                        'sub_index': sub_index,
                        'sub_time': sub_time,
                        'sub_text': sub_text,
                        }   

            return render(request, 'highlight/subtitle.html', context)

        if 'index' in post_key:
            startIndex = request.POST.get('index')
            print(startIndex, type(startIndex))
           

            startTime = sub_time[int(startIndex)-1]
            startTime = startTime.split('-->')[0].split('.')[0]
            startTime_list = startTime.replace('0','').split(':')
            print('list', startTime_list)
            startTime_second = 1
            hournum = 0
            minutenum = 0
            secondnum = 0
            for i, time in enumerate(startTime_list):
                if time != '':
                    if i == 0:
                        hournum = 3600 * int(time)
                    if i == 1:
                        minutenum = 60 * int(time)
                    if i == 2:
                        secondnum = int(time)
            startTime_second = hournum +minutenum +secondnum
            print('second',round(int(startTime_second), 3) )
            context = {'startTime' : round(int(startTime_second), 3)}
            # return render(request,'highlight/subtitle.html', context )
            return JsonResponse(context)

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

        # make video with subtitle
        if args['flag'] =='test':
            return render(request, 'highlight/last.html')
        else: 
            make_result = makeVideo.saveSrt(args,time_dict,text_dict)
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

