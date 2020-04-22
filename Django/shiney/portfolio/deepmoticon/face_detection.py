import dlib, cv2, sys
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from imutils import paths
from . import light_emoticon
from .import flex_emoticon
# import sweat_emoticon
# import goodday_emoticon
# import hand_emoticon
# import chicken_emoticon
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

def dog_face_detection(args, i, filename, max_img):
    print('dog_face_detection start')
    SCALE_FACTOR = 0.2


    detector = dlib.cnn_face_detection_model_v1(args['model_path'] + 'dog_face_detection/dogHeadDetector.dat')
    predictor = dlib.shape_predictor(args['model_path'] +'dog_face_detection/landmarkDetector.dat')

    drawframe = max_img.copy()
    img = cv2.cvtColor(drawframe, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, dsize=None, fx=SCALE_FACTOR, fy=SCALE_FACTOR)

    dets = detector(img, upsample_num_times=1)

    print('dets' ,len(dets))
    if len(dets)== 0:
        flag = 'not'
        circle_img = circle_make(args, i, filename, max_img)
        return max_img, circle_img, flag

    else:
        flag = 'ok'
        for j, d in enumerate(dets):
                    
            # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

            x1, y1 = int(d.rect.left() / SCALE_FACTOR), int(d.rect.top() / SCALE_FACTOR)
            x2, y2 = int(d.rect.right() / SCALE_FACTOR), int(d.rect.bottom() / SCALE_FACTOR)

            cv2.rectangle(drawframe, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=(255,0,0), lineType=cv2.LINE_AA)

            shape = predictor(img, d.rect)
            shape = face_utils.shape_to_np(shape)

            right_p = shape[2]
            left_p = shape[5]
            nose_p = shape[3]
            
            cv2.circle(drawframe, center=tuple((left_p / SCALE_FACTOR).astype(int)), radius=5, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            left_eye =tuple((left_p / SCALE_FACTOR).astype(int))

            cv2.circle(drawframe, center=tuple((right_p / SCALE_FACTOR).astype(int)), radius=5, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            right_eye =tuple((right_p / SCALE_FACTOR).astype(int))
            
            cv2.circle(drawframe, center=tuple((nose_p / SCALE_FACTOR).astype(int)), radius=5, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            nose =tuple((nose_p / SCALE_FACTOR).astype(int))
            
            # imshow('drawframe', drawframe)
            
            savepath = args['output_path'] +f'{filename}/2.face_detection_{i}_{filename}.jpg' 
            cv2.imwrite(savepath, drawframe)
            
            square_img = square_make(args, i, filename, max_img, left_eye, right_eye,nose)
            
            ##### light_emoticon 실행
            light_emoticon.wear_sunglass(args,i, filename,max_img.copy(), left_eye, right_eye,nose)
            flex_emoticon.wear_cap(args, i, filename,max_img.copy(), left_eye, right_eye, nose)
            
            # imshow('check', square_img)
            circle_img = circle_make(args, i, filename, square_img)
            return square_img, circle_img, flag

def circle_make(args, i, filename, square_img):
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
    # imshow('circle', circle_img)
    savepath = args['output_path'] +f'{filename}/2.circle_img_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, circle_img)
    return circle_img


def square_make(args, i, filename, max_img, left_eye, right_eye,nose):

    ##### face_crop
    eye_width = abs(right_eye[0] - left_eye[0] )
    print(eye_width)
    # center_x = left_eye [1]+ int((right_eye[1]-left_eye[1])/2)

    center_y = min(right_eye[1], left_eye[1]) + int(abs(right_eye[1] - nose[1])/2)            
    
    margin = int(1.5 * eye_width)

    left = max(0, nose[0] - margin) 
    right = min(max_img.shape[1],   nose[0] + margin)
    top = max(0, center_y - margin)
    bottom = min(max_img.shape[0],  center_y + margin)

    print(left, right, top, bottom)
    face_img = max_img[top:bottom, left:right]

    # left_dist = np.abs(0- left)
    # right_dist = np.abs(max_img.shape[1] - right)
    # top_dist = np.abs(0-top)
    # bottom_dist = np.abs(max_img.shape[0]- bottom)

    # print(left_dist, right_dist, top_dist, bottom_dist)
    # min_dist = min([left_dist, right_dist, top_dist, bottom_dist])
    
    # # if min_dist >= 30:
    # #     min_dist = 30

    # left = left-min_dist
    # right = right + min_dist
    # top = top-min_dist
    # bottom = bottom + min_dist
    # print(left, right, top, bottom)

    # face_img = max_img[top: bottom, left: right]

    face_img= round_box(args, i, filename, face_img)
    # print(face_img.shape)
    # imshow('face_img', face_img)
    savepath = args['output_path'] +f'{filename}/2.square_img_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, face_img)

    return face_img


                

def round_box(args, i, filename, max_img):

    fg_img = max_img
    bg_img =cv2.imread(args['item_path'] + 'mask.jpg', 1)
   
    bg_img =cv2.resize(bg_img, (fg_img.shape[1],fg_img.shape[0]), )

    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(bg_gray, 100, 255, cv2.THRESH_BINARY)
    mask_inv = 255-mask

    fg_img2 = cv2.bitwise_and(fg_img, fg_img, mask=mask_inv)
    bg_img2 = cv2.bitwise_and(bg_img, bg_img, mask = mask)

    round_img = cv2.add(fg_img2, bg_img2)
   
    savepath =args['output_path']+ f'{filename}/1.round_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, round_img)

    return round_img

    