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


def wear_sunglass(args,i, filename,square_img, left_eye, right_eye,nose):
    
    width =  np.abs(right_eye[0] - left_eye[0])
    eye_left = max(0, left_eye[0]-int(0.5*(width)))
    eye_right = min(square_img.shape[1], right_eye[0]+int(0.5*(width)))
    eye_top=max(0, min(left_eye[1], right_eye[1])-int(0.4*width))
    eye_bottom = min(square_img.shape[0], max(left_eye[1], right_eye[1])+int(0.4*width))

    # print(eye_elft, eye_right, eye_top, eye_bottom)
    eye_part = square_img[eye_top: eye_bottom, eye_left: eye_right] 
    
    # imshow('eye_part', eye_part)
    
    item = cv2.imread(args['item_path']+'sunglasses.jpg')
    item = cv2.resize(item, (eye_part.shape[1], eye_part.shape[0]),interpolation=cv2.INTER_AREA)

    itemgray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(itemgray, 100, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    img1_bg = cv2.bitwise_and(eye_part, eye_part, mask=mask)
    img2_fg = cv2.bitwise_and(item, item, mask = mask_inv)

    des = cv2.add(img1_bg, img2_fg)

    square_img[eye_top: eye_bottom, eye_left: eye_right] = des
    sunglass_img=square_img
    # imshow('', sunglass_img)
    savepath = args['output_path'] + f'{filename}/3.sunglass_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, sunglass_img)

    # print(right_eye, left_eye, nose, square_img.shape)

    ##### face_crop
    eye_width = abs(right_eye[0] - left_eye[0] )
    # print(eye_width)
    # center_x = left_eye [1]+ int((right_eye[1]-left_eye[1])/2)

    center_y = min(right_eye[1], left_eye[1]) + int(abs(right_eye[1] - nose[1])/2)            
    
    margin = int(1.5 * eye_width)

    left = max(0, nose[0] - margin) 
    right = min(square_img.shape[1],   nose[0] + margin)
    top = max(0, center_y - margin)
    bottom = min(square_img.shape[0],  center_y + margin)

    face_img = square_img[top:bottom, left:right]
    # print(face_img.shape)
    # imshow('face_img', face_img)

    flag2 = 'square'
    light(args,i, filename, face_img,flag2)



    # return sunglass_img


def light(args, i, filename, square_img , flag2):
    if flag2 == 'square':
        fg_img = square_img

        bg_img =cv2.imread(args['item_path'] + 'circle_mask.png', 1)
    
        bg_img =cv2.resize(bg_img, (fg_img.shape[1],fg_img.shape[0]), )

        bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(bg_gray, 100, 255, cv2.THRESH_BINARY)
        mask_inv = 255-mask

        print(fg_img.shape, mask_inv.shape)

        fg_img2 = cv2.bitwise_and(fg_img, fg_img, mask=mask_inv)
        bg_img2 = cv2.bitwise_and(bg_img, bg_img, mask = mask)

        circle_img = cv2.add(fg_img2, bg_img2)
    else:
        circle_img = square_img

    circle_img = cv2.resize(circle_img, (300,300,))

    #print('circle', circle_img.shape)
    new_img = np.full((400,400,3), 255, dtype = np.uint8)

    new_img[50:-50, 50:-50,:] = circle_img
    #print(new_img.shape)

    #imshow('', new_img)
    savepath = args['output_path'] + f'{filename}/4.circle_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, circle_img)

    # imshow('circle_img', circle_img)

    mp4_make(args,i,filename, circle_img)

def mp4_make(args,i, filename, circle_img):
    

    frame_array= []
    light_list = [args['item_path'] + 'light111.png',
                  args['item_path'] + 'light222.png',
                 args['item_path'] + 'light111.png',
                  args['item_path'] + 'light222.png']

    text_list = [args['item_path'] + 'text1.jpg',
                args['item_path'] + 'text2.jpg',
                args['item_path'] + 'text3.jpg',
                args['item_path'] + 'text4.jpg']

    for light_path, text_path in zip(light_list, text_list):
        # print(light_path, text_path)
        final_img = light_text(args, i, filename, circle_img, light_path, text_path)
        frame_array.append(final_img)
    # print(len(frame_array))    

    for s in range(5):
        for light_path in light_list:
            final_img = light_text(args, s, filename,circle_img, light_path, args['item_path'] +'text4.jpg' )
            frame_array.append(final_img)
    
    # print(len(frame_array))
            
    pathOut = args['output_path'] + f'{filename}/5.light_text_{i}_{filename}.mp4'
    fps = 5
    size = (480,480)
    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()    


def light_text(args, i, filename, circle_img, light_path, text_path):
    mask = cv2.imread(args['item_path'] + 'light_mask.png', 0) # 480
    mask = np.expand_dims(mask, -1)

    bg_img =cv2.imread(light_path, 1)  # 480

    img2 = cv2.resize(circle_img, (430,430))
    circle_img2 = np.full((480, 480, 3), 255, dtype = 'uint8')
    circle_img2[25:-(25), 25:-(25)]=img2
    # print(mask.shape, circle_img2.shape, bg_img.shape)
    light_img = np.where(mask<10, circle_img2, bg_img)
    text = cv2.imread(text_path, 1)
    text_img = np.where(text>100,light_img, text )

    return text_img
