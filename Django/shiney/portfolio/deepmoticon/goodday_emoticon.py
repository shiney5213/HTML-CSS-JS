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



def heart_box(args, i, filename, max_box):
    fg_img = np.ones((480,480,3), dtype = 'uint8')
    max_box =cv2.resize(max_box, (150,150) )
    # fg_img[140:310, 150:320]=max_box
    fg_img[150:300, 160:310]=max_box

    # imshow('', fg_img)

    bg_img =cv2.imread(args['item_path'] + 'heart-mask.jpg', 1)
   
    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(bg_gray, 100, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    fg_img2 = cv2.bitwise_and(fg_img, fg_img, mask=mask_inv)
    bg_img2 = cv2.bitwise_and(bg_img, bg_img, mask = mask)

    heart_img = cv2.add(fg_img2, bg_img2)
    # print(heart_img.shape)
    savepath = args['output_path'] + f'{filename}/8_1.goodday_{i}_{filename}.jpg' 
    print(savepath)
    cv2.imwrite(savepath, heart_img)
    # imshow('round_img', heart_img)

    goodday_video(args, i, filename, heart_img)


def goodday_video(args, i, filename, heart_img):

    cap = cv2.VideoCapture(args['item_path'] +'goodday.avi')

    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    
    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :

            bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(bg_gray, 230, 255, cv2.THRESH_BINARY)
            mask_inv = 255-mask

            fg_img2 = cv2.bitwise_and(heart_img, heart_img, mask=mask)
            # imshow('fg', fg_img2)
            bg_img2 = cv2.bitwise_and(frame, frame, mask = mask_inv)

            goodday_img = cv2.add(fg_img2,bg_img2) 

            if j % 100 == 0:
                savepath = args['output_path'] + f'{filename}/8_1.goodday_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, goodday_img)
                # imshow('good', goodday_img)

            frame_array.append(goodday_img)
            j +=1
        else:
            break
            
    print(len(frame_array))
    cap.release()

    pathOut = args['output_path'] + f'{filename}/8_2.goodday_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()    