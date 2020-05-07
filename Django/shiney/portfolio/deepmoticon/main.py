import dlib, cv2, sys
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from imutils import paths
# from face_detection import dlib_face_detection
# from face_detection import start_face_detection
from . import dog_detection
from . import face_detection
from . import sweat_emoticon
from . import chicken_emoticon
from . import hand_emoticon
from . import goodday_emoticon
from . import light_emoticon
from . import flex_emoticon
from . import wait_emoticon
#from . import face_funit
#from . import classification_test
# import argparse
from multiprocessing import Process


def imshow(tit, image):
    plt.title(tit)
    plt.axis('off') 
    if image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    else:
        plt.imshow(image, cmap = 'gray')
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='data path information'
    )
    parser.add_argument('--input_path',  default = '../../static/portfolio/deepmoticon/', type=str,
                        help='path to the input image path')
    parser.add_argument('--input_img',default='dog2.jpg', 
                        type=str,  help='path to the image index path')
    parser.add_argument('--model_path', default='./model/', 
                        type=str,  help='base_model')  
    parser.add_argument('--item_path',  default = './items/' ,
                        type = str,  help='path to the save file path')
    parser.add_argument('--output_path', default = '../../static/portfolio/deepmoticon/result/', type=str,
                        help='batch_size')
    parser.add_argument('--funit_model_path',default='./funit/configs/', 
                        type=str,  help='number of epoch')
    parser.add_argument('--confThreshold', default=0.5, type=int,
                        help='img_height')
    parser.add_argument('--maskThreshold', default=0.5, type=int,
                        help='img_width')
    parser.add_argument('--mopology_iter', default=20, type=int,
                        help='img_width')
    parser.add_argument('--class_id', default='dog', type=str,
                        help='img_width')

    args = parser.parse_args()
    return args


def deepmoticon_start(input_img):
    # args = parse_args()
    # input image

    args = {'input_path':'./static/portfolio/deepmoticon/',
            'input_img': input_img, 
            'model_path':'./portfolio/deepmoticon/model/', 
            'item_path': './portfolio/deepmoticon/items/' ,
            'output_path': './static/portfolio/deepmoticon/',
            'funit_model_path':'./portfolio/deepmoticon/funit/configs/',
            'confThreshold': 0.5,
            'maskThreshold': 0.5,
            'mopology_iter': 20, 
            'class_id': 'dog'
            }

    # image: chihuahua, collie, darkshund, golden_retriever, jindodog, maltese, poodle, pug, shih_tzu, welshcorgi
    img_path = args['input_path'] + args['input_img']   
    filename = os.path.basename(img_path).replace('.jpg', '').replace('.png', '')
    # print(img_path, filename)
    # print('abs',os.path.abspath(args['output_path']))
    dirname = os.path.join(args['output_path'] ,filename)
    # print('dirname', dirname)
    # os.mkdir(dirname)
    
    try:
        os.mkdir(dirname)
    except Exception as err:
        pass

    frame = cv2.imread(img_path, 1)

    cv2.imwrite(args['output_path'] +f'./{filename}/0.ordinary_{filename}.jpg', frame)

    max_img_list, segmen_img_list = dog_detection.mrcnn(args, filename, frame)
    print( len(max_img_list))

    for i, (segmen_img, max_img) in enumerate(zip(segmen_img_list, max_img_list)):
        # imshow('max', max_img)

    #     ##### segmentation으로 할 경우
    #     # chicken_emoticon.segmentation_make(args, i, filename, segmen_img, max_img)


        face_img, circle_img, flag2 = face_detection.dog_face_detection(args, i, filename, max_img)
        # imshow('circle_img', circle_img)
        # imshow('face_img', face_img)

        p = Process(target=chicken_emoticon.circle_img_make, args = (args, i, filename, circle_img.copy(), max_img))
        p.start()
        p.join()

        
        q = Process(target=goodday_emoticon.heart_box, args=(args, i, filename, face_img.copy()))
        q.start()
        q.join()

        if flag2 == 'ok':
            r= Process(target=hand_emoticon.hand_video, args =(args, i, filename, max_img.copy()))
            r.start()
            r.join()
            s = Process(target=sweat_emoticon.sweat_video, args =(args, i, filename, max_img.copy()))
            s.start()
            s.join()
        else:
            light_emoticon.light(args,i, filename,max_img.copy(), 'circle')
            sweat_emoticon.sweat_video2(args, i, filename, max_img.copy())
            flex_emoticon.flex_video(args, i, filename,max_img.copy())
            wait_emoticon.wait_video(args, i, filename, max_img.copy())





    
    
    
    # for max_img in max_img_list:
    #     imshow('max', max_img)
    
    # ######square_img: light_emoticon/goodday_emoticon=> 얼굴찾아서 하기
    # for i, square_img in enumerate(square_img_list):
    #     imshow('square_img', square_img)
    #     flags= ['light', 'goodday', 'chicken' ]
    #     # flags = ['light']
    #     face_detection.dog_face_detection(args, i, filename, square_img, flags)


    # ####### max_img : flex_emoticon/sweat_emoticon/max_emoticon
    # for i , max_img in enumerate(max_img_list):
    #     imshow('max_img', max_img)
    #     img = max_img.copy()
    #     flags = ['flex', 'sweat','hand']
    #     face_detection.dog_face_detection(args, i, filename, max_img, flags)
    #     # face_detection.dog_face_detection(args, i, filename, max_img, 'sweat')
        

    #     # classiciaction
    #     # dog_breed, breed_rate = classification_test.load_model_weight(args,max_img)
    #     # print(dog_breed, breed_rate)

    #     # if breed_rate >= 0.5:
    #     #     funit_img_dict = face_funit.generator(args, i, filename, img, dog_breed)
    #     #     pass
