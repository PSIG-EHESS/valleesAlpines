# -*- coding: utf-8 -*-

#==============================================================================
# Programme permttant de déterminer les contours majoritaires d'images traitées 
# par l'algorithme de Sobel sous forme de fonctions implémentées.
#
# Entrée:
# Path d'un fichier d'images avec la bibliothèque "matplotlib.image"
#
# Sortie:
# Fichier texte contenant le nom des images et leur attribut en bois
# Temps de traitement du programme
#==============================================================================

#---------- Importations ----------#
import time
import glob
import contours_sobel3 as cs2


#---------- Fonctions ----------#
def nb_pixels_contours(img):
    """
    Fonction permettant de compter le nombre de pixels appartenant aux contours
    de l'image en relief
    """
    pxc = 0
    for i in range(img.shape[0]): #rows
        for j in range(img.shape[1]): #columns
            if img[i,j] != 0:
                pxc += 1
    return pxc

def bois_major(pxc_h, pxc_v):
    """
    Fonction permettant de déterminer si les contours sont principalement 
    verticaux ou horizontaux
    """
    if pxc_h < pxc_v:
        return "vertical"
    elif pxc_h == pxc_v:
        return "identiques"
    else:
        return "horizontal"


#---------- Test ----------#
if __name__ == "__main__":
   tic = time.time()
   
   # Ouverture du fichier
   file = open("bois_hv.txt", 'w')
   
   # Traitement des images
   filepath = glob.glob("./Test_bois_hv/*.jpg")
   compteur = 1
   for i in filepath:
       print(compteur,"/",len(filepath))
       # Ouverture de l'image en B&W
       M = cs2.img_gray(i)
       # Génération des contours
       img_h = cs2.sobel_h(M,i)[0]
       img_v = cs2.sobel_v(M,i)[0]
       # Nombre de pixels des contours
       pxc_h = nb_pixels_contours(img_h)
       pxc_v = nb_pixels_contours(img_v)
       # Détermination des contours majoritaires
       maj = bois_major(pxc_h, pxc_v)
       
       # Ecriture dans le fichier
       file.write("\n")
       file.write(i)
       file.write(";")
       file.write(maj)
       compteur += 1
     
   # Fermeture du fichier
   file.close()

   toc = time.time()
   print ('%.3f sec elapsed ' % (toc-tic))