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

def mrcnn(args, filename, frame):

    # confThreshold = 0.5 # score(확률값) 확인
    # maskThreshold = 0.4  # mask 확인
    classesFile = args['model_path'] + 'mrcnn/mscoco_labels.names'
    classes = None
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')

    # 그래프 구조
    textGraph = args['model_path'] + 'mrcnn/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt'
    # weight 파일
    modelWeights = args['model_path'] + 'mrcnn/frozen_inference_graph.pb'

    # Load the network
    net = cv2.dnn.readNetFromTensorflow(modelWeights, textGraph)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    class_ID = classes.index(args['class_id'])
    max_img_list, segmen_img_list=mrcnn_segmentation(args,filename, frame, class_ID, net)
    
    # imshow('drawBox', square_img)
    return  max_img_list, segmen_img_list


def mrcnn_segmentation(args,filename, frame, class_ID, net):
    blob = cv2.dnn.blobFromImage(frame, swapRB=True, crop=False)
    net.setInput(blob)
    boxes, masks = net.forward(['detection_out_final', 'detection_masks'])
    max_img_list, segmen_img_list=postprocess(args, filename, frame, class_ID, boxes, masks)
    return  max_img_list, segmen_img_list
    
def postprocess(args, filename, frame,class_ID, boxes, masks):
    numClasses = masks.shape[1]
    numDetections = boxes.shape[2]

    frameH = frame.shape[0]
    frameW = frame.shape[1]

    segmen_img_list = []
    max_img_list = []
    for i in range(numDetections):
        box = boxes[0, 0, i]  # 7개 정보  ?, classid, score, left, top 
        mask = masks[i]
        score = box[2]

        if score > args['confThreshold']:
            classId = int(box[1])
            # print(classId, class_id)
            if classId == class_ID:
                # Extract the bounding box
                left = int(frameW * box[3])
                top = int(frameH * box[4])
                right = int(frameW * box[5])
                bottom = int(frameH * box[6])

                left = max(0, min(left, frameW - 1))
                top = max(0, min(top, frameH - 1))
                right = max(0, min(right, frameW - 1))
                bottom = max(0, min(bottom, frameH - 1))
                # Extract the mask for the object
                classMask = mask[classId]
                # print('classMask')
                # Draw bounding box, colorize and show the mask on the image
                segmen_img, max_img = drawBox(args,i,filename, frame, score, left, top, right, bottom, classMask )
                # imshow('postprocess', square_img)
                segmen_img_list.append(segmen_img)

                max_img_list.append(max_img)
    return  max_img_list, segmen_img_list
            
def drawBox(args, i,filename, frame, score, left, top, right, bottom, classMask):

    #####max_img
    x_center = int((right-left)/2)
    y_center = int((bottom-top)/2)
    width = int(right-left)
    height = int(bottom - top)

    # square box
    if width> height:
        left = int(left + (width-height)/2)
        right = int(right - (width-height)/2)
    else:
        bottom = int(top + width)

    square_img = frame[top:bottom+1, left:right+1]
    # imshow('square_img', square_img)

    savepath = args['output_path'] + '{filename}/1.square_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, square_img) 

    left_dist = np.abs(0- left)
    right_dist = np.abs(frame.shape[1] - right)
    top_dist = np.abs(0-top)
    bottom_dist = np.abs(frame.shape[0]- bottom)

    print(frame.shape)
    print(left_dist, right_dist, top_dist, bottom_dist)
    min_dist = min([left_dist, right_dist, top_dist, bottom_dist])
    
    # if min_dist >= 30:
    #     min_dist = 30

    left = left-min_dist
    right = right + min_dist
    top = top-min_dist
    bottom = bottom + min_dist

    max_img = frame[top: bottom, left: right]
    # imshow('max_box', max_img)
    # print(max_img.shape)

    savepath = args['output_path'] + f'{filename}/1.max_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, max_img)
    max_img = round_box(args, i, filename, max_img)
     
    
    ##### segmen_img
    classMask = cv2.resize(classMask, (max_img.shape[1], max_img.shape[0]))
    
#     for maskThreshold in maskThreshold_list:
    mask = (classMask > args['maskThreshold'])
    mask = np.expand_dims(mask, axis = -1)

    only_dog = np.where(mask==1, max_img, 255)
    savepath = args['output_path'] + f'{filename}/1.segmen_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, only_dog)
    # imshow('', only_dog)

    return only_dog, max_img


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
   
    savepath =args['output_path'] + f'{filename}/1.round_{i}_{filename}.jpg' 
    cv2.imwrite(savepath, round_img)

    return round_img
