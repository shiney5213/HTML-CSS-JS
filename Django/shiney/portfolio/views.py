from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View



# Create your views here.

def index(request):
	return HttpResponse('portfolio 보자!')




class portfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/port_main.html')

    # def post(self, request):
    #     file = request.FILES.get('filename', '')
    #     filename = file._name

    #     if file == '':
    #         return HttpResponse('file을 다시 upload해주세요')
    #     else:
    #         fp = open(settings.BASE_DIR + '/static/portfolio/' + filename, 'wb')
    #         for chunk in file.chunks():
    #             fp.write(chunk)
    #         fp.close()
         
    #     context= {'data': filename}

    #     # return HttpResponse('file upload success')
    #     return render(request, 'portfolio/image_result.html', context)



# def index(request):
#     file = request.FILES.get('filename', '')
#     filename = file._name

#     if file == '':
#         return HttpResponse('file을 다시 upload해주세요')
#     else:
#         fp = open(settings.BASE_DIR + '/static/portfolio/' + filename, 'wb')
#         for chunk in file.chunks():
#             fp.write(chunk)
#         fp.close()

#     return HttpResponse('file upload success')

# class UploadView(View):
#     def get(self, request):
#         return render(request, 'portfolio/image_upload.html')

#     def post(self, request):
#         file = request.FILES.get('filename', '')
#         filename = file._name

#         if file == '':
#             return HttpResponse('file을 다시 upload해주세요')
#         else:
#             fp = open(settings.BASE_DIR + '/static/portfolio/' + filename, 'wb')
#             for chunk in file.chunks():
#                 fp.write(chunk)
#             fp.close()
         
#         context= {'data': filename}

#         # return HttpResponse('file upload success')
#         return render(request, 'portfolio/image_result.html', context)
