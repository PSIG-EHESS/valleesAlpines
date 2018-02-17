# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:00:33 2018

@author: Pierre
"""


#création du csv
def createCSV():
    '''
    fonction createCSV:
        utilité: fonction qui renvoie un csv appelé rendu.csv
        return: rendu.csv; fichier csv de la forme ['ImageName','Date','MaskName','ImageCutName','ImageHorizontalSobelName','ImageVerticalSobelName','HorizontalPixelNumber','VerticalPixelNumber','DirectionPlanches']
    '''
    file = open("rendu.csv", 'w')
    titre = ['ImageName n','Date','MaskName','ImageCutName','ImageHorizontalSobelName','ImageVerticalSobelName','HorizontalPixelNumber','VerticalPixelNumber','DirectionPlanches']
    ligne = ";".join(titre)+"\n"
    file.write(ligne)
    file.close()
    
#écriture dans le csv
def writeCSV(liste):
    '''
    fonction writeCSV:
        utilité: fonction qui écrit à la suite du fichier rendu.csv déjà créé
        paramètres: liste; liste de strings correspondant à la forme ['ImageName','MaskName','ImageCutName','ImageHorizontalSobelName','ImageVerticalSobelName','HorizontalPixelNumber','VerticalPixelNumber','DirectionPlanches']
        return: rien (complète juste le fichier csv déjà existant)
    '''
    file = open("rendu.csv", 'a')
    ligne = ";".join(liste)+"\n"
    file.write(ligne)
    file.close()