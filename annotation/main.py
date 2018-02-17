# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:39:40 2017

@author: Pierre
"""
import decoupeBis as d
import kerasRunning as k
import reconstitutionIm as r
import traitements as trait
import write_csv as WC
import glob
import os
import effetBord as s
import date as da
from scipy import misc

def main(file, target, imgW,imgL,name):
    '''
    fonction main:
        utilité: fonction qui prend en entrée une image de chalet et renvoie en sortie le chalet de cette image
        découpé de l'arrière plan. Puis effectue les traitements(Sobel) et détermine si les planches du chalet sont horizontales ou verticales
        paramètres: file; l'emplacement de l'image à traiter.
                    target; emplacement et nom du masque du chalet de l'image.
                    imgW; largeur de l'image.
                    imgL; longeur de l'image.
                    name; emplacement et nom de l'image en sortie.
        return: masque: une image du masque du chalet.
                chalet: l'image du chalet découpée de son arrière plan.
                sobel_h: l'image issue du filtre de sobel horizontal
                sobel_v: l'image issue du filtre de sobel vertical
                csv: un fichier csv qui retourne les chemins des images précédentes dans les dossiers, le nombre de pixels horizontaux, verticaux ainsi que la direction des planches
    '''
    
    # étapes d'execution de l'algorithme
        #1 découpage de l'image initiale en imagettes
    liste_csv = []
    liste_prov1 = d.decoupe(file).split('\\')
    liste_csv += [liste_prov1[len(liste_prov1)-1]]
        #2 ecriture de la date dans csv
    date = da.date(file)
    liste_csv += [str(date)]
        #3 test de l'appartenance des imagettes à la classe chalet ou non via le classifieur construit précédemment
    k.running(imgW,imgL)
        #4 constitution du masque de probabilité d'appartenance au chalet de l'image initiale
    liste_prov2 = r.reconstitution(file, target).split('\\')
    liste_csv += [liste_prov2[len(liste_prov2)-1]]
        #5 reconstitution de l'image du chalet découpé de l'arrière plan à partir du masque construit
    liste_prov3 = s.effetdebords(file,target,name).split("\\")
    liste_csv += [liste_prov3[len(liste_prov3)-1]]
        #6 traitements images sur la zone du chalet (filtres de sobel) pour déterminer la direction des planches
    liste_csv += trait.traitements ('Rendu\\imageCoupe\\'+name)
    WC.writeCSV(liste_csv)
    print('img_done')
    
if __name__ == "__main__":
    
    #♣traitement successif de toutes les images présentes dans le fichier Test_bois_hv
    WC.createCSV()    
    filepath = glob.glob('Test_bois_hv\*.jpg')
    for j in range(0,len(filepath)):
        files=glob.glob('Test\*.jpg')
        for a in range(0,len(files)):
            os.remove(files[a])
        files2=os.listdir('Test/TestChalet')
        for a in range(0,len(files2)):
            os.remove('Test/TestChalet/'+files2[a])
        im = misc.imread(filepath[j])
        imgW,imgL = len(im[0]),len(im)
        name_trait = filepath[j].split('.')
        name_trait2 = name_trait[0].split('\\')
        main(filepath[j],name_trait2[1]+'masque.jpg',imgW,imgL,name_trait2[1]+'imageDecoup.jpg')
