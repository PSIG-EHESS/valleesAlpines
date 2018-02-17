# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:14:57 2017

@author: Pierre
"""


import numpy as np
from scipy import misc
import glob
from os.path import basename, splitext

def reconstitution(filenameImage,target):
    '''
    fonction reconstitution:
        utilité: constitution du masque de probabilité d'appartenance de chaque pixel de l'image à la zone du chalet
        paramètres: filenameImage; nom de l'image de départ
                    target; nom de l'image du masque
        return: masque; l'image du masque du chalet dans l'image.
                target; nom de l'image du masque
    '''
    filepath = glob.glob('Test\TestChalet\*.jpg')
    filename = filenameImage
    imageIni = misc.imread(filename)
    listeFin = []
    for a in range(0,len(imageIni)):
        y=[]
        for b in range(0,len(imageIni[0])):
            y+=[[0,0,0]]
        listeFin+=[y]
    for i in range(0,len(filepath)):
        listeName = filepath[i].split("\\")
        name = listeName[len(listeName)-1]
        listeName = name.split('.')
        listeName = listeName[0].split('g')
        listeName = listeName[1].split(',')
        listeName = [int(listeName[0]),int(listeName[1])]
        for l in range(listeName[0],listeName[0]+200):
            for c in range(listeName[1],listeName[1]+200):
                listeFin[l][c][0] += 1
                listeFin[l][c][1] += 1
                listeFin[l][c][2] += 1
    misc.imsave('Rendu\\masque\\'+target, listeFin)   
    return(target)