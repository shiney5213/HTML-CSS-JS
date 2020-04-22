import dlib, cv2, sys
from imutils import face_utils,rotate
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



def sweat_video(args, i, filename, round_img ):
# left_eye, right_eye, nose
    cap = cv2.VideoCapture(args['item_path'] + 'sweat.avi')
    # min_left_eye = min(left_eye)
    # cap.set(3,min_left_eye )
    # cap.set(4,min_left_eye )

    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    
    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :
            if j in [s for s in range(5,45)]:
                round_img =text_plus(args, round_img, j,filename)
            
            mask = frame
            # print('mask', mask.shape)

            # imshow('mask', mask)

            fg_img = np.zeros((480,480,3), dtype = 'uint8')
            
            mask = cv2.resize(mask, (130,130))
            # mask = rotate(mask, 45)

            fg_img[0: 130, 0: 130] = mask

            #imshow('', mask)
            bg_img = cv2.resize(round_img, (480,480))

            sweat_img = np.where(fg_img<100, bg_img, fg_img)
            if j % 100 == 0 :
                savepath = args['output_path'] + f'{filename}/6_1.sweat_{j}_{filename}.jpg' 
                cv2.imwrite(savepath, sweat_img)
                savepath =  args['output_path'] + f'{filename}/6_1.chromakey_{j}_{filename}.jpg' 
                cv2.imwrite(savepath, mask)

            frame_array.append(sweat_img)
            j +=1
        else:
            break
            
        
    # print(len(frame_array))
    cap.release()

        
    pathOut =  args['output_path'] + f'{filename}/6_2.sweat_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(100):
        out.write(frame_array[i])
    out.release()    


def sweat_video2(args, i, filename, round_img ):    
    frame_array = []
    j = 0
    for j in range(400):
        if j % 4==0:
            new_img =np.full((480,480, 3),255, dtype = np.uint8)
            round_img = cv2.resize(round_img, (480-j, 480-j))
            
            new_img[int(j/2):480-int(j/2),int(j/2):480-int(j/2)] = round_img

        if j in [s for s in range(5,45)]:
            round_img =text_plus(args, round_img, j,filename)

        frame_array.append(new_img)
         
    pathOut =  args['output_path'] + f'{filename}/6_2.sweat_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(100):
        out.write(frame_array[i])
    out.release() 


def text_plus(args, round_img, j, filename):
    
    text_path =  args['item_path'] + f'text{int(j/5)}{int(j/5)}.jpg'
    text_img = cv2.imread(text_path, 1)
    # print(text_img.shape)
    #imshow('text_img', text_img)
    
    round_img= cv2.resize(round_img, (480,480))
    
    text_gray = cv2.cvtColor(text_img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(text_gray, 250, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    round_img2 = cv2.bitwise_and(round_img, round_img, mask=mask)
    
    text_img2 = cv2.bitwise_and(text_img, text_img, mask = mask_inv)

    text_plus_img = cv2.add(round_img2, text_img2)
    if j % 100 == 0 :
        savepath = args['output_path'] + f'{filename}/6_1.text_{j}_{filename}.jpg' 
        cv2.imwrite(savepath, text_img)
        savepath = args['output_path'] + f'{filename}/6_1.text2_{j}_{filename}.jpg' 
        cv2.imwrite(savepath, text_plus_img)
    #imshow('text_plus_img',text_plus_img)
        
    return text_plus_img
    