# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:02:22 2017

@author: Pierre
"""

from PIL import Image
import random as rd
import glob
from os.path import basename, splitext
 
#algorithme qui coupe des grandes images d'un dossier en zones de 200 pixels de manière aléatoire
filepath = glob.glob('D:\projetRecherche\entrainement\Classif\ToutesImages\*.jpg')
for i in range(0,len(filepath)):
    im = Image.open(filepath[i])
    width = 200
    height = 200
    for j in range (0,3):
        left = rd.randint(0,im.size[0]-200)
        top = rd.randint(0,im.size[1]-200)
        box = (left, top, left+width, top+height)
        area = im.crop(box)
        area.save('D:\projetRecherche\entrainement\Classif\ImDecoup\img{},{}.jpg'.format(i,j))