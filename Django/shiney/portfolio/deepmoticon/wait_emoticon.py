import dlib, cv2, sys
from imutils import face_utils, rotate
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from imutils import paths
import argparse


def imshow(tit, image):
    plt.title(tit)
    plt.axis('off') 
    if image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    else:
        plt.imshow(image, cmap = 'gray')
    plt.show()
    

def wait_video(args, i, filename, round_img):

    cap = cv2.VideoCapture(args['item_path'] +'wait.avi')
    round_img = cv2.resize(round_img, (480,480))
    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    
    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :
            
            bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(bg_gray, 250, 255, cv2.THRESH_BINARY)
            mask_inv = 255-mask

            fg_img2 = cv2.bitwise_and(round_img, round_img, mask=mask)
            # imshow('fg', fg_img2)
            bg_img2 = cv2.bitwise_and(frame, frame, mask = mask_inv)

            wait_img = cv2.add(fg_img2,bg_img2) 

            if j % 100 == 0:
                savepath = args['output_path'] +f'{filename}/11_1.wait_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, frame)
                
                savepath = args['output_path'] +f'{filename}/11_1.wait_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, fg_img2)

                savepath = args['output_path'] +f'{filename}/11_1.wait_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, wait_img)
                # imshow('wait_img', wait_img)

            frame_array.append(wait_img)
            j +=1
        else:
            break
            
    print(len(frame_array))
    cap.release()

    pathOut = args['output_path'] + f'{filename}/11_2.wait_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    

    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()