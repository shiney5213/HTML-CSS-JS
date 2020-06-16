from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def crop(args, save_start, save_end):
    # crop 처리
    filename = args['filename']
    crop_filename = filename.replace('.mp4', '_2.mp4')


    old_path = args['video_root'] + filename
    new_path = args['video_root'] + crop_filename

    # print('old', os.path.isfile(old_path))


    clip = VideoFileClip(old_path).subclip(float(save_start), float(save_end))
    clip.write_videofile(new_path)

    return crop_filename