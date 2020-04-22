import dlib, cv2, sys
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from imutils import paths
# import argparse


def imshow(tit, image):
    plt.title(tit)
    plt.axis('off') 
    if image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    else:
        plt.imshow(image, cmap = 'gray')
    plt.show()

def wear_cap(args, i, filename,face_detect, left_eye, right_eye, nose):
    
    width =  np.abs(right_eye[0] - left_eye[0])
    #print('width', width)
    cap_left = max(0, left_eye[0]-int(0.9*(width)))
    cap_right = min(face_detect.shape[1], right_eye[0]+int(0.9*(width)))
    cap_top =max(0,left_eye[1]-int(1.2*width))
    cap_bottom= min(face_detect.shape[0], left_eye[1]+int(0.5 * width))

    cap_part = face_detect[cap_top: cap_bottom, cap_left: cap_right] 
    #print(cap_left, cap_right, cap_top, cap_bottom)
    #print(cap_part.shape)

    item = cv2.imread(args['item_path'] + 'cap3.jpg')
    #print('item',item.shape)
    item = cv2.resize(item, (cap_part.shape[1], cap_part.shape[0]),interpolation=cv2.INTER_AREA)
    
    itemgray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(itemgray, 230, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    img1_bg = cv2.bitwise_and(cap_part, cap_part, mask=mask)
    img2_fg = cv2.bitwise_and(item, item, mask = mask_inv)

    des = cv2.add(img1_bg, img2_fg)

    face_detect[cap_top: cap_bottom, cap_left: cap_right] = des
    cap_img=face_detect
    #imshow('', cap_i/mg)
    cap_img = chain_draw(args ,i, filename, cap_img, left_eye, right_eye, nose)

    money_video(args, i, filename, cap_img)

def chain_draw(args,i, filename, cap_img, left_eye, right_eye, nose):

   # chain 그리기
    width =  np.abs(right_eye[0] - left_eye[0])
    chain_left = max(0, left_eye[0]-int(0.5*(width)))
    chain_right = min(cap_img.shape[1], right_eye[0]+int(0.5*(width)))
    chain_top = max(0, nose[1]+ int(0.5*width))
    chain_bottom =min(cap_img.shape[0], nose[1]+int(2.0*(width)))
   
    chain_part = cap_img[ chain_top:  chain_bottom,  chain_left:  chain_right] 
   

    if chain_part.shape[0] > 50 :
        # imshow('cap', cap_img)
        savepath = args['output_path'] + f'{filename}/5_1.cap_{i}_{filename}.jpg' 
        cv2.imwrite(savepath, cap_img)

        money_video(args, i, filename, cap_img)

        #imshow('', chain_part)
        item = cv2.imread(args['item_path'] + 'chain6.jpg')
        item = cv2.resize(item, (chain_part.shape[1], chain_part.shape[0]),interpolation=cv2.INTER_AREA)

        itemgray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(itemgray, 230, 255, cv2.THRESH_BINARY)
        mask_inv = 255-mask

        img1_bg = cv2.bitwise_and(chain_part, chain_part, mask=mask)
        img2_fg = cv2.bitwise_and(item, item, mask = mask_inv)

        des = cv2.add(img1_bg, img2_fg)

        cap_img[chain_top:  chain_bottom,  chain_left:  chain_right] = des
        chain_img=cap_img
        #imshow('', chain_img)
        
        savepath = args['output_path'] + f'{filename}/5_1.cap_{i}_{filename}.jpg' 
        cv2.imwrite(savepath, chain_img)
        return chain_img
    else:
        return cap_img


def money_video(args, i, filename, cap_img):

    cap = cv2.VideoCapture(args['item_path'] + 'money4.mp4')
    # cap = cv2.VideoCapture('./items/shiney.avi')


    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    
    frame_array = []
    for j in range(1000):
        ret, frame = cap.read()
        
        if ret:
            # print(frame.shape)
            mask = frame[200:680, 400:880]
            
            bg_img =cap_img
            bg_img = cv2.resize(bg_img, (480,480))
        #mask = cv2.resize(mask, (480,480))

            money_img = np.where(mask<5, bg_img, mask)
            # imshow('', money_img)
            
            frame_array.append(money_img)
        else:
            break

    # print(len(frame_array))
    cap.release()
        
    pathOut = args['output_path'] + f'{filename}/5_6.flex_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


def coin_make(args, i, filename, max_box):
    

    item = cv2.imread(args['item_path'] + 'coins2.jpg')
    item = cv2.resize(item, (max_box.shape[1], max_box.shape[0]))
    # print('tem',item.shape)

    itemgray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(itemgray, 230, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    img1_bg = cv2.bitwise_and(max_box, max_box, mask=mask)
    img2_fg = cv2.bitwise_and(item, item, mask = mask_inv)

    des = cv2.add(img1_bg, img2_fg)

    coin_img=des
#    imshow('', coin_img)
    
    savepath = args['output_path'] + f'{filename}/5_2.coin2_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, coin_img)
    
    round_box(i, filename, coin_img)

def flex_video(args, i, filename, round_img):

    cap = cv2.VideoCapture(args['item_path'] +'flex.avi')
    round_img = cv2.resize(round_img, (480,480))
    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
    
    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :
            
            bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(bg_gray, 5, 255, cv2.THRESH_BINARY)
            mask_inv = 255-mask

            fg_img2 = cv2.bitwise_and(frame, frame, mask=mask)
            # imshow('fg', fg_img2)
            bg_img2 = cv2.bitwise_and(round_img, round_img, mask = mask_inv)

            wait_img = cv2.add(fg_img2,bg_img2) 

            if j % 100 == 0:
                savepath = args['output_path'] +f'{filename}/11_1.flex_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, frame)
                
                savepath = args['output_path'] +f'{filename}/11_1.flex_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, fg_img2)

                savepath = args['output_path'] +f'{filename}/11_1.flex_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, wait_img)
                # imshow('wait_img', wait_img)

            frame_array.append(wait_img)
            j +=1
        else:
            break
            
    print(len(frame_array))
    cap.release()

    pathOut = args['output_path'] + f'{filename}/11_2.flex_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)
    

    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
