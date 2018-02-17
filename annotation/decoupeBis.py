# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:01:04 2017

@author: Pierre
"""

from PIL import Image
import glob
from os.path import basename, splitext


def decoupe(filenameImage):
    '''
    fonction decoupe:
        utilité: fonction découpant l'image de départ en petites imagettes
        paramètres: filenameImage; l'emplacement de l'image de départ
        return: filenameImage; l'emplacement de l'image de départ (pas malin désolé)
    '''
    filename = filenameImage
    im = Image.open(filename)
    long = im.size[0]
    larg = im.size[1]
    for i in range (0,larg-200,50):
        for j in range (0,long-200,50):
            box = (j,i,j+200,i+200)
            area = im.crop(box)
            area.save('Test\img{},{}.jpg'.format(i,j))
    return(filenameImage)