import dlib, cv2, sys
from imutils import face_utils, rotate
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from imutils import paths

def imshow(tit, image):
    plt.title(tit)
    plt.axis('off') 
    if image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    else:
        plt.imshow(image, cmap = 'gray')
    plt.show()



def hand_video(args, i, filename, round_img):

    cap = cv2.VideoCapture(args['item_path'] + 'hand2.avi')

    # print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    round_img = cv2.resize(round_img, (480,480))
    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :
            
            bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(bg_gray, 240, 255, cv2.THRESH_BINARY)
            mask_inv = 255-mask
            # print(round_img.shape, mask.shape)
            fg_img2 = cv2.bitwise_and(round_img, round_img, mask=mask)
            # imshow('fg', fg_img2)
            bg_img2 = cv2.bitwise_and(frame, frame, mask = mask_inv)

            hand_img = cv2.add(fg_img2,bg_img2) 

            if j % 100 == 0:
                savepath = args['output_path'] + f'{filename}/9._1.frame_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, frame)
                
                savepath = args['output_path'] + f'{filename}/9_1.mask_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, fg_img2)

                savepath = args['output_path'] + f'{filename}/9_1.hand_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, hand_img)
                # imshow('hand', hand_img)

            frame_array.append(hand_img)
            j +=1
        else:
            break
            
    # print(len(frame_array))
    cap.release()

    pathOut = args['output_path'] + f'{filename}/9_2.hand_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()   

