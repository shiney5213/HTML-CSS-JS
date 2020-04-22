import warnings
warnings.filterwarnings('ignore')
from tensorflow.keras.models import model_from_json, load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input 
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import cv2
import argparse



def load_model_weight(args, test_img):

    date = '200417_2'
    model_path = args.model_path + f'classification/{date}.json'
    weight_path = args.model_path + f'classification/200417_2_04_0.9818.h5'
    
    with open(model_path, 'r') as json_file:
        loaded_model_json =json_file.read()

    model = model_from_json(loaded_model_json)
    model.load_weights(weight_path)

    dog_breed, breed_rate = predict_testimg(args, test_img,model)
    return dog_breed, breed_rate

def predict_testimg(args, test_img, model):

    target = ['chihuahua','collie','dachshunds','golden_retriever','jindodog','maltese','poodle','pug','shih-tzu','welshcorgi']
    # test_path = '../images/dog1.jpg'
    # test_img = load_img(test_path, target_size = (299,299))
    # test_img = img_to_array(test_img)
    test_img = cv2.resize(test_img, (299,299))
    test_img = np.expand_dims(test_img, axis=0)
    test_img = preprocess_input(test_img)
    
    predict = model.predict(test_img)
    max_index = np.argmax(predict, 1)
    dog_pred = target[max_index[0]]
    # print(dog_pred, np.max(predict))
    return dog_pred,np.max(predict)

