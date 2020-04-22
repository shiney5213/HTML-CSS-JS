import cv2
import numpy as np
import os
import sys
import random
from matplotlib import pyplot as plt
# import argparse


def imshow(tit, image):
    plt.title(tit)
    plt.axis('off') 
    if image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    else:
        plt.imshow(image.reshape(image.shape[0],image.shape[1]), cmap = 'gray')
    plt.show()

def chicken_start(args, i, filename, square_img)  :
    
    segmen_img, square_img = start_segmentation(args, i, filename,square_img)

    gray = cv2.cvtColor(segmen_img, cv2.COLOR_RGB2GRAY)
    ret, mask = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY)
    # imshow('', mask)


    ##### mopology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    # open
    # result = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, ) 
    # 침색
    result = cv2.erode(mask, kernel, iterations = 10)
    # 팽창
    # result = cv2.dilate(result, kernel, iterations = 5)

    # close
    # result = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # imshow('', result)

def start_segmentation(args, i, filename, square_img):
    classesFile = args['model_path'] + "mrcnn/mscoco_labels.names"
    classes = None
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')

    # 그래프 구조
    textGraph = args['model_path'] + "mrcnn/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt"
    # weight 파일
    modelWeights = args['model_path'] + "mrcnn/frozen_inference_graph.pb"   # 다운받아야 함

    # Load the network
    net = cv2.dnn.readNetFromTensorflow(modelWeights, textGraph)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # confThreshold = 0.5 # score(확률값) 확인
    # maskThreshold = 0.2  # mask 확인
    # img_path = '../../images/dog1.jpg'
    # frame = cv2.imread(img_path, 1)

    frame = square_img
    blob = cv2.dnn.blobFromImage(frame, swapRB=True, crop=False)
    net.setInput(blob)

    boxes, masks = net.forward(['detection_out_final', 'detection_masks'])
    segmen_img, square_img=postprocess(args, i, filename, frame, boxes, masks)
    # imshow('segmen', segmen_img)

    small_img, mask_img = mopology_img(args,i, segmen_img,square_img)
    chicken_video(args, i, filename, small_img, mask_img)
    return segmen_img, square_img


def chicken_video(args, i, filename, small_img, mask_img):

    cap = cv2.VideoCapture(args['item_path'] + 'chicken.avi')

    print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

    frame_array = []
    j = 0
    while (1):
        ret, frame = cap.read()        
        if ret :
            # bg_gray = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
            # imshow('bg', bg_gray)
            # ret, mask = cv2.threshold(bg_gray, 255, 255, cv2.THRESH_BINARY)
            # imshow('mask', mask)
            mask = mask_img
            mask_inv = 255-mask
            # print(frame.shape, mask.shape)
            fg_img2 = cv2.bitwise_and(frame, frame, mask=mask)
    #         imshow('fg', fg_img2)
            bg_img2 = cv2.bitwise_and(small_img, small_img, mask = mask_inv)

            chicken_img = cv2.add(fg_img2,bg_img2) 
            # imshow('chicken',chicken_img)

            if j % 100 == 0:
                savepath = args['output_path'] + f'{filename}/1.chicken_{i}_{j}{filename}.jpg'
                cv2.imwrite(savepath, chicken_img)
                # imshow('chicken_img', chicken_img)

            frame_array.append(chicken_img)
            j +=1
        else:
            break

    print(len(frame_array))
    cap.release()

    pathOut = args['output_path'] + f'{filename}/10_2.chicken_{i}_{filename}.mp4'
    fps = 30
    size = (480,480)

    
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'X', '2', '6', '4'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()    

def segmentation_make(args,i,filename, segmen_img, square_img):
    gray = cv2.cvtColor(segmen_img, cv2.COLOR_RGB2GRAY)
    ret, mask = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY)
    # imshow('', mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    
    #####mopology
    # open
    # result = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, ) 
    
    # 침색
    result = cv2.erode(mask, kernel, iterations = args['mopology_iter'])
    
    # 팽창
    # result = cv2.dilate(result, kernel, iterations = 5)

    # close
    # result = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # imshow('', result)
    result = np.expand_dims(result, -1)
    # print(result.shape)

    mopo_img = np.where(result==0, square_img, 255)
    small_make(args, i, filename, mopo_img, result)

def circle_img_make(args,i,filename, circle_img, square_img):
    gray = cv2.cvtColor(circle_img, cv2.COLOR_RGB2GRAY)
    # ret, mask = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY)
    # mask = np.expand_dims(mask, -1)

    mask = cv2.imread(args['item_path']+ 'circle_mask.png', 0)
    # mopo_img = np.where(result==0, square_img, 255)
    small_make(args, i, filename, circle_img, mask)


def small_make(args,i,filename, dog_img, mask):
    small_img = np.full((480,480, 3),255, dtype = np.uint8)
    mask_img = np.full((480,480, 1),255, dtype = np.uint8)

    dog_img= cv2.resize(dog_img, (240,240))
    mask = cv2.resize(mask, (240,240))
    mask = np.expand_dims(mask, -1)
    small_img[240:,120:360]=dog_img
    mask_img[240:,120:360]=mask

    chicken_video(args, i, filename, small_img, mask_img)
   
    return small_img, mask_img





