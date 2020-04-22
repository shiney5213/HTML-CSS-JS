import os
import numpy as np
from PIL import Image
import copy

import torch
import torch.backends.cudnn as cudnn
from torchvision import transforms
import torch.nn.functional as F

from funit.utils import get_config
from funit.trainer import Trainer

import yaml

import torch
import torch.nn as nn
import torch.nn.init as init

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import cv2
import matplotlib.pyplot as plt
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


def generator(args, i, filename, img, dog_breed):
    #imshow('', img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if len(img.shape)==3:
        img = img.reshape((1,) + img.shape)
    
    datagen = ImageDataGenerator(
        samplewise_center=False,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,
        zca_whitening=False,
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        channel_shift_range=0.1,
        fill_mode='nearest',
        horizontal_flip=False,
        vertical_flip=False,
        rescale=None,
        preprocessing_function=None)
        
    output = f'./result/{filename}/generator/'
    if not os.path.exists(output):
        os.makedirs(output)

    i = 0
    for batch in datagen.flow(img, batch_size=1,
                              save_to_dir= output,
                              save_prefix='dog',
                              save_format='jpg'):
        i += 1
        if i > 10:
            break

    funit_img_dict = funit_make(args,i, filename, dog_breed)
    return funit_img_dict

def funit_make(args,i, filename, dog_breed):
    expression = ['fun','smile', 'sad', 'shock', 'sleep']
    # expression = [ 'smile3']
    
    config = args.funit_model_path + 'funit_animals.yaml'
    ckpt = args.funit_model_path + 'animal119_gen_00100000.pt'
    class_image_folder = args.output_path + f'{filename}/generator'
    #input = f'./items/{flag}.jpg/'
    #output = f'./result/{filename}/funit_img_{flag}_{i}.jpg'
    config = get_config(config)
    config['batch_size'] = 1
    config['gpus'] = 1
    cudnn.benchmark = True


    trainer = Trainer(config)
    #print(type(trainer))
    #trainer.cuda()
    trainer.load_ckpt(ckpt)
    trainer.eval()

    transform_list = [transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    transform_list = [transforms.Resize((200, 200))] + transform_list
    transform = transforms.Compose(transform_list)

    #print('Compute average class codes for images in %s' % class_image_folder)


    images = os.listdir(class_image_folder)
    for k, f in enumerate(images):
        fn = os.path.join(class_image_folder, f)
        img = Image.open(fn).convert('RGB')
    #     img_tensor = transform(img).unsqueeze(0).cuda()
        img_tensor = transform(img).unsqueeze(0)

        with torch.no_grad():
            class_code = trainer.model.compute_k_style(img_tensor, 1)
            if k == 0:
                new_class_code = class_code
            else:
                new_class_code += class_code
    final_class_code = new_class_code / len(images)


    funit_img_dict = {}
    for express in expression:
        input = args.item_path + f'expression/{dog_breed}/{express}.png'
        output = args.output_path + f'{filename}/funit_img_{dog_breed}_{express}_{i}.jpg'
        image = Image.open(input)
        image = image.convert('RGB')
        content_img = transform(image).unsqueeze(0)

        #print('Compute translation for %s' % input)

        with torch.no_grad():
            output_image = trainer.model.translate_simple(content_img, final_class_code)
            #print(output_image.shape)
            #print(content_img.shape)
            image = output_image.detach().cpu().squeeze().numpy()
            image = np.transpose(image, (1, 2, 0))
            image = ((image + 1) * 0.5 * 255.0)
            output_img = Image.fromarray(np.uint8(image))
            output_img.save(output, 'JPEG', quality=99)
            funit_img_dict[str(express)]= output
            print('Save output t/o %s' % output)

    return funit_img_dict
