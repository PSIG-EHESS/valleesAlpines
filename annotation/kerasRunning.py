# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:44:00 2017

@author: Pierre
"""

import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential,load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np

img_width = 200
img_height = 200

def running(imgW,imgL):
    '''
    fonction running:
        utilité: classifie les imagettes composant une image. Deux classes possibles; chalet, pas chalet. Ainsi, cette fonction prédit si une imagette fait ou non partie de la zone du chalet
        paramètres: imgW, imgL; hauteur et largeur des imagettes
    '''
    model = load_model('model.h5')
    wid=imgW//img_width
    hei=imgL//img_height
    liste=[]
    for i in range (0,imgL-200,50):
        for j in range (0,imgW-200,50):
            img = keras.preprocessing.image.load_img('Test\img{},{}.jpg'.format(i,j), target_size=(img_width, img_height))
            x = keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict_classes(images, batch_size=10)
            if classes[0][0]==1:
                img.save('Test\TestPasChalet\img{},{}.jpg'.format(i,j))
            else:
                img.save('Test\TestChalet\img{},{}.jpg'.format(i,j))