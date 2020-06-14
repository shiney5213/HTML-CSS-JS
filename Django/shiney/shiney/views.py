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
# from . import apps
import shutil
import random

def home(request):
    return render(request, 'home.html')

