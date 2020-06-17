import time
import boto3
import urllib.request, json 
import uuid
import requests
import json
import re, os
import codecs
from time import gmtime, strftime
from moviepy.editor import *
from moviepy import editor
from moviepy.video.tools.subtitles import SubtitlesClip, TextClip
from time import gmtime, strftime
import numpy as np

def upload_file(audio_file, args,  object_name=None):
    #upload file in s3
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # audio_file = args['audio_file']
    bucket = args['bucket']
    file_name = args['audio_root']+args['audio_file']
    # job_name = args['job_name']

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3',
                    aws_access_key_id = args['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key = args['AWS_SECRET_ACCESS_KEY'],
                    region_name = args['AWS_DEFAULT_REGION'])
    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def createTranscribeJob(args, mediaUri, mediaFile):
    # audio to text by AWS trancribe 
    job_name = args['job_name'] 
    region  = args['region'] 
    bucket = args['bucket'] 
    print('mediaUri',mediaUri)

    # Set up the Transcribe client 
    transcribe = boto3.client('transcribe',
                    aws_access_key_id = args['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key = args['AWS_SECRET_ACCESS_KEY'],
                    region_name = args['AWS_DEFAULT_REGION'])
  
    
    print( "Creating Job: " + "transcribe" + mediaFile + " for " + mediaUri )
    
    # Use the uuid functionality to generate a unique job name.  Otherwise, the Transcribe service will return an error
    response = transcribe.start_transcription_job( TranscriptionJobName=job_name, 
        LanguageCode = "ko-KR", 
        MediaFormat = "mp3", 
        Media = { "MediaFileUri" : mediaUri }, 
        )
    
    print(response)
    
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    print(status)
    
    return status

def getTranscript( transcriptURI ):
    # Get the resulting Transcription Job and store the JSON response in transcript
    result = requests.get( transcriptURI )

    return result.text    


def newPhrase():
	return { 'start_time': '', 'end_time': '', 'words' : [] }

def getTimeCode( seconds ):
	t_hund = int(seconds % 1 * 1000)
	t_seconds = int( seconds )
	t_secs = ((float( t_seconds) / 60) % 1) * 60
	t_mins = int( t_seconds / 60 )
	return str( "%02d:%02d:%02d,%03d" % (00, t_mins, int(t_secs), t_hund ))

def getPhrasesFromTranscript( transcript ):

    # This function is intended to be called with the JSON structure output from the Transcribe service.  However,
    # if you only have the translation of the transcript, then you should call getPhrasesFromTranslation instead

    # Now create phrases from the translation
    ts = json.loads( transcript )
    items = ts['results']['items']
    
    #set up some variables for the first pass
    phrase =  newPhrase()
    phrases = []
    nPhrase = True
    x = 0
    c = 0

    print("==> Creating phrases from transcript...")

    for item in items:

        # if it is a new phrase, then get the start_time of the first item
        if nPhrase == True:
            if item["type"] == "pronunciation":
                phrase["start_time"] = getTimeCode( float(item["start_time"]) )
                nPhrase = False
            c+= 1
        else:    
            # We need to determine if this pronunciation or puncuation here
            # Punctuation doesn't contain timing information, so we'll want
            # to set the end_time to whatever the last word in the phrase is.
            # Since we are reading through each word sequentially, we'll set 
            # the end_time if it is a word
            if item["type"] == "pronunciation":
                phrase["end_time"] = getTimeCode( float(item["end_time"]) )
                
        # in either case, append the word to the phrase...
        phrase["words"].append(item['alternatives'][0]["content"])
        x += 1
        
        # now add the phrase to the phrases, generate a new phrase, etc.
        if x == 10:
            #print c, phrase
            phrases.append(phrase)
            phrase = newPhrase()
            nPhrase = True
            x = 0
            
    return phrases

def writeTranscriptToSRT( transcript, sourceLangCode, srtFileName ):
    # Write the SRT file for the original language
    print( "==> Creating SRT from transcript")
    phrases = getPhrasesFromTranscript( transcript )
    # print(phrases)
    writeSRT( phrases, srtFileName )

    return phrases

def writeSRT( phrases, filename ):
    print( "==> Writing phrases to disk...")
    # open the files
    e = codecs.open(filename,"w+", encoding='utf-8')

    x = 1

    for phrase in phrases:
        print(phrase)

        # determine how many words are in the phrase
        length = len(phrase["words"])

        # write out the phrase number
        e.write( str(x) + "\n" )
        x += 1

        # write out the start and end time
        e.write( phrase["start_time"] + " --> " + phrase["end_time"] + "\n" )

        # write out the full phase.  Use spacing if it is a word, or punctuation without spacing
        out = getPhraseText( phrase )

        # write out the srt file
        e.write(out + "\n\n" )


        #print out
    e.close()

def getPhraseText( phrase ):

	length = len(phrase["words"])
		
	out = ""
	for i in range( 0, length ):
		if re.match( '[a-zA-Z0-9]', phrase["words"][i]):
			if i > 0:
				out += " " + phrase["words"][i]
			else:
				out += phrase["words"][i]
		else:
			out += phrase["words"][i]
	return out
	    

def startSTT(args, crop_filename):
    s3 = boto3.resource('s3')
    
 
    
    audio_file = args['audio_root'] + args['audio_file']
    print('audio_file is', os.path.isfile(audio_file))
    ### upload file s3
    upload_result = upload_file(audio_file, args, object_name=None)
    print('upload', upload_result)

    ### transcibe in AWS
    MediaFormat  = 'mp3'
    # # mediaUri = f"s3://eyshin/{args['audio_file']}"
    mediaUri = f"s3://eyshin/{audio_file}"
    mediaFile = 'test_audio'

    # mediaFile = args['dirname']

    if args['flag']=='test':
        subtitles_file = args['video_root']+args['subtitles_file']
        with open(subtitles_file, 'r', encoding = 'UTF-8') as f:
            subtitle = f.read()

        subtitle = subtitle.replace("'", '')
        subtitle_list = subtitle.split('\n\n')
        print(len(subtitle_list))

        sub1 = []
        for sub in subtitle_list:
            if sub !='' :
                sub1.append(sub.split('\n'))
        print('sub1', sub1, len(sub1))

        sub_index = []
        sub_time = []
        sub_text = []

        for (index, time, text) in sub1:
            sub_index.append(index)
            sub_time.append(time.replace(',','.'))
            sub_text.append(text.replace(',','.'))

    else:
        status = createTranscribeJob( args, mediaUri, mediaFile)
        if status['TranscriptionJob']['TranscriptionJobStatus'] =='COMPLETED':
            ### get transcript result in asw Uri
            transcript_Uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
            ### transcript result
            transcript = getTranscript(str(transcript_Uri))

            ### save src file
            subtitles_file = args['video_root']+args['subtitles_file']
            print('subpath', subtitles_file)
            transcript_dict = writeTranscriptToSRT(transcript, 'ko-KR', subtitles_file)
            # print(transcript_dict)

            with open(subtitles_file, 'r', encoding = 'UTF-8') as f:
                subtitle = f.read()

            subtitle = subtitle.replace("'", '')
            subtitle_list = subtitle.split('\n\n')
            print(len(subtitle_list))

            sub1 = []
            for sub in subtitle_list:
                if sub !='' :
                    sub1.append(sub.split('\n'))
            print('sub1', sub1, len(sub1))

            sub_index = []
            sub_time = []
            sub_text = []

            for (index, time, text) in sub1:
                sub_index.append(index)
                sub_time.append(time.replace(',','.'))
                sub_text.append(text.replace(',','.'))

    print(len(sub_text), sub_text)
    return sub_index, sub_time, sub_text


