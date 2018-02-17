# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:04:29 2017

@author: Pierre
"""
import numpy as np
from scipy import misc
def effetdebords(imIni,zones,name):
    '''
    fonction effedebords:
        utilité: reconstitution de l'image du chalet à partir de l'image du masque trouvée précédemment
        paramètres: imIni; nom de l'image initiale
                    zones; image du masque
                    name; nom de l'image du chalet découpée de son arrière plan
        return: name; nom de l'image du chalet découpée de son arrière plan
    '''
    listeFin = misc.imread('Rendu\\masque\\'+zones)
    imageIni = misc.imread(imIni)
    for pixLigne in range(0,len(listeFin)):
        for pixCol in range(0,len(listeFin[0])):
            if listeFin[pixLigne][pixCol][0] >= 10:
                listeFin[pixLigne][pixCol][0] = imageIni[pixLigne][pixCol][0]
                listeFin[pixLigne][pixCol][1] = imageIni[pixLigne][pixCol][1]
                listeFin[pixLigne][pixCol][2] = imageIni[pixLigne][pixCol][2]
            else:
                listeFin[pixLigne][pixCol][0] = 0
                listeFin[pixLigne][pixCol][1] = 0
                listeFin[pixLigne][pixCol][2] = 0
    misc.imsave('Rendu/imageCoupe/'+name, np.asarray(listeFin))
    return(name)