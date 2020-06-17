import time
import boto3
import urllib.request, json 
import uuid
import requests
import json
import re
import codecs
from time import gmtime, strftime
from moviepy.editor import *
from moviepy import editor
from moviepy.video.tools.subtitles import SubtitlesClip, TextClip
from time import gmtime, strftime
import numpy as np
global infile

def saveSrt(args,time_dict,text_dict):
    
    final_sub = []
    for i in range(1,len(time_dict)+1):
        row = []
        for  time, text in zip( time_dict.values(), text_dict.values()):
            row.append(str(i))
            row.append(time)
            row.append(text)
            print('row',row)
            row_final = '\\n'.join(row)
    final_sub.append(row_final)
    final_subtitle = '\\n\\n'.join(final_sub)
    print('final_subtitle',final_subtitle)

    print(final_subtitle)

    subtitles_file2 = args['video_root']+args['subtitles_file2']


    print(subtitles_file2)

    e = codecs.open(subtitles_file2,"w+", encoding='utf-8')
    e.write(final_subtitle)
    e.close()

    return os.path.isfile(subtitles_file2)

class SubtitlesClip2(VideoClip):
    """ A Clip that serves as "subtitle track" in videos.
    
    One particularity of this class is that the images of the
    subtitle texts are not generated beforehand, but only if
    needed.

    Parameters
    ==========

    subtitles
      Either the name of a file, or a list

    Examples
    =========
    
    >>> from moviepy.video.tools.subtitles import SubtitlesClip
    >>> from moviepy.video.io.VideoFileClip import VideoFileClip
    >>> generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=24, color='white')
    >>> sub = SubtitlesClip("subtitles.srt", generator)
    >>> myvideo = VideoFileClip("myvideo.avi")
    >>> final = CompositeVideoClip([clip, subtitles])
    >>> final.write_videofile("final.mp4", fps=myvideo.fps)
    
    """

    def __init__(self, subtitles, make_textclip=None):
        
        VideoClip.__init__(self, has_constant_size=False)

        if isinstance(subtitles, str):
            subtitles = file_to_subtitles(subtitles)

        #subtitles = [(map(cvsecs, tt),txt) for tt, txt in subtitles]
        self.subtitles = subtitles
        self.textclips = dict()

        if make_textclip is None:
            make_textclip = lambda txt: TextClip(txt, font='MDotum',
                                        fontsize=30, color='white',
                                        stroke_color='black', 
                                        stroke_width=0.5,)

        self.make_textclip = make_textclip
        self.start=0

        try:
            self.duration = max([tb for ((ta,tb), txt) in self.subtitles])
        except:
            self.dutraion =  VideoFileClip(infile).duration

        self.end=self.duration
        
        def add_textclip_if_none(t):
            """ Will generate a textclip if it hasn't been generated asked
            to generate it yet. If there is no subtitle to show at t, return
            false. """
            sub =[((ta,tb),txt) for ((ta,tb),txt) in self.textclips.keys()
                   if (ta<=t<tb)]
            if not sub:
                sub = [((ta,tb),txt) for ((ta,tb),txt) in self.subtitles if
                       (ta<=t<tb)]
                if not sub:
                    return False
            sub = sub[0]
            if sub not in self.textclips.keys():
                self.textclips[sub] = self.make_textclip(sub[1])

            return sub

        def make_frame(t):
            sub = add_textclip_if_none(t)
            return (self.textclips[sub].get_frame(t) if sub
                    else np.array([[[0,0,0]]]))

        def make_mask_frame(t):
            sub = add_textclip_if_none(t)
            return (self.textclips[sub].mask.get_frame(t) if sub
                    else np.array([[0]]))
        
        self.make_frame = make_frame
        hasmask = bool(self.make_textclip('T').mask)
        self.mask = VideoClip(make_mask_frame, ismask=True) if hasmask else None

    def in_subclip(self, t_start= None, t_end= None):
        """ Returns a sequence of [(t1,t2), txt] covering all the given subclip
        from t_start to t_end. The first and last times will be cropped so as
        to be exactly t_start and t_end if possible. """

        def is_in_subclip(t1,t2):
            try:
                return (t_start<=t1<t_end) or (t_start< t2 <=t_end)
            except:
                return False
        def try_cropping(t1,t2):
            try:
                return (max(t1, t_start), min(t2, t_end))
            except:
                return (t1, t2)
        return [(try_cropping(t1,t2), txt) for ((t1,t2), txt) in self.subtitles
                                               if is_in_subclip(t1,t2)]
    


    def __iter__(self):
        return iter(self.subtitles)
    


    def __getitem__(self, k):
        return self.subtitles[k]

    

    def __str__(self):

        def to_srt(sub_element):
            (ta, tb), txt = sub_element
            fta = cvsecs(ta)
            ftb = cvsecs(tb)
            return "%s - %s\n%s"%(fta, ftb, txt)
        
        return "\n\n".join(to_srt(s) for s in self.subtitles)
    


    def match_expr(self, expr):

        return SubtitlesClip2([e for e in self.subtitles
                              if re.findall(expr, e[1]) != []])
    

    def write_srt(self, filename):
        with open(filename, 'w+', encoding = 'UTF-8') as f:
            f.write(str(self))


def file_to_subtitles(filename):
    """ Converts a srt file into subtitles.

    The returned list is of the form ``[((ta,tb),'some text'),...]``
    and can be fed to SubtitlesClip.

    Only works for '.srt' format for the moment.
    """
    times_texts = []
    current_times = None
    current_text = ""
    with open(filename,'r', encoding = 'UTF-8') as f:
        for line in f:
            times = re.findall("([0-9]*:[0-9]*:[0-9]*,[0-9]*)", line)
            if times:
                current_times = [cvsecs(t) for t in times]
            elif line.strip() == '':
                times_texts.append((current_times, current_text.strip('\n')))
                current_times, current_text = None, ""
            elif current_times:
                current_text += line
    return times_texts

def createVideo( originalClipName, subtitlesFileName, outputFileName, alternateAudioFileName, useOriginalAudio=True ):
	# This function is used to put all of the pieces together.   
	# Note that if we need to use an alternate audio track, the last parm should = False
	
	print( "\n==> createVideo " )

	# Load the original clip
	print( "\t" + strftime("%H:%M:%S", gmtime()), "Reading video clip: " + originalClipName )
	clip = VideoFileClip(originalClipName)
	print( "\t\t==> Original clip duration: " + str(clip.duration))

	if useOriginalAudio == False:
		print( strftime( "\t" + "%H:%M:%S", gmtime()), "Reading alternate audio track: " + alternateAudioFileName)
		audio = AudioFileClip(alternateAudioFileName)
		audio = audio.subclip( 0, clip.duration )
		audio.set_duration(clip.duration)
		print( "\t\t==> Audio duration: " + str(audio.duration))
		clip = clip.set_audio( audio )
	else:
		print (strftime( "\t" + "%H:%M:%S", gmtime()), "Using original audio track...")
		
	# Create a lambda function that will be used to generate the subtitles for each sequence in the SRT
# 	generator = lambda txt: TextClip(txt, font='Arial-Bold', fontsize=24, color='white')
	generator = lambda txt: TextClip(txt, font='MDotum', fontsize=30, color='white')

	# read in the subtitles files
	print( "\t" + strftime("%H:%M:%S", gmtime()), "Reading subtitle file: " + subtitlesFileName )

	print('subtitlesFileName',subtitlesFileName)
	print('generator',generator)
	subs = SubtitlesClip2(subtitlesFileName, generator)
	print ("\t\t==> Subtitles duration before: " + str(subs.duration))
	subs = subs.subclip( 0, clip.duration - .001)
	subs.set_duration( clip.duration - .001 )
	print ("\t\t==> Subtitles duration after: " + str(subs.duration))
	print ("\t" + strftime("%H:%M:%S", gmtime()), "Reading subtitle file complete: " + subtitlesFileName )

	print('subs', subs)
	print( "\t" + strftime( "%H:%M:%S", gmtime()), "Creating Subtitles Track...")
	annotated_clips = [annotate(clip.subclip(from_t, to_t), txt) for (from_t, to_t), txt in subs]
    
    
	print ("\t" + strftime( "%H:%M:%S", gmtime()), "Creating composited video: " + outputFileName)
	# Overlay the text clip on the first video clip
	
	final = concatenate_videoclips( annotated_clips )
	

	print( "\t" + strftime( "%H:%M:%S", gmtime()), "Writing video file: " + outputFileName )
	final.write_videofile(outputFileName)

def annotate(clip, txt, txt_color='white', fontsize=30, font='MDotum'):
    # Writes a text at the bottom of the clip  'Xolonium-Bold'
    txtclip = editor.TextClip(txt, fontsize=fontsize, font=font, color=txt_color).on_color(color=[0,0,0])
    cvc = editor.CompositeVideoClip([clip, txtclip.set_pos(('center', 50))])
    return cvc.set_duration(clip.duration)


def mergeVideo(args ):
    global infile
    subtitles_file =args['video_root']+ args['subtitles_file']
#    infile = args['vedio_root'] + args['crop_//filename']
    infile = args['video_root'] + args['filename']

    print('in', os.path.isfile(infile))

    outfilename = args['video_root'] + args['final_filename']
    mp3_filename = args['audio_root']+ args['audio_file']

    print('mp3_filename', os.path.isfile(mp3_filename))
    print('subtitles_file', os.path.isfile(subtitles_file))


    createVideo(infile, subtitles_file, outfilename , mp3_filename, True)

    if os.path.isfile( outfilename):
        return True




