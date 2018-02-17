# -*- coding: utf-8 -*-

#==============================================================================
# Programme permttant d'utiliser les contours d'images traitées par 
# l'algorithme de Sobel sous forme de fonctions implémentées.
#
# Entrée:
# Path d'une image avec la bibliothèque "matplotlib.image"
#
# Sortie:
# Temps de traitement du programme
#
# Possibilité d'afficher et de sauvegarder les traitements en décommentant les 
# lignes utilisant la bibliothèque "matplotlib.pyplot".
#==============================================================================

#---------- Importations ----------#
import time
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc


#---------- Lecture de l'image en niveaux de gris ----------#
def img_gray(url):
    img = mpimg.imread(url)
    
    M = np.zeros((img.shape[0],img.shape[1]))
    M[:,:] = img[:,:,0]

#    plt.imshow(M, cmap = plt.get_cmap('gray'))
#    plt.title("B&W Picture")
#
#    #plt.savefig("B&W_img.png")
#    plt.show()
    
    return M


#---------- Filtre de Sobel ----------#
def sobel(M, url):
    edges = filters.sobel(M)

#    fig, ax = plt.subplots()
#    ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
#    ax.set_title('Sobel Edge Detection')
#    name = "Traitements/Sobel_" + url.replace("./Test_bois_hv2/","")
#    plt.savefig(name)
#    plt.show()
#    return [edges, name]

    return edges
    

#---------- Sobel horizontaux ----------#
def sobel_h(M, url):
    edges_h = filters.sobel_h(M)
    
#    fig, ax = plt.subplots()
#    ax.imshow(edges_h, cmap=plt.cm.gray, interpolation='nearest')
#    ax.set_title('Horizontal Sobel Edge Detection')
    name = "Traitements/Sobel_h_" + url.replace("Rendu\\imageCoupe\\","")
    misc.imsave(name,edges_h)
#    plt.savefig(name)
#    plt.show()
    return [edges_h,name]
    

#---------- Sobel verticaux ----------#
def sobel_v(M, url):
    edges_v = filters.sobel_v(M)

#    fig, ax = plt.subplots()
#    ax.imshow(edges_v, cmap=plt.cm.gray, interpolation='nearest')
#    ax.set_title('Vertical Sobel Edge Detection')

    name = "Traitements/Sobel_v_" + url.replace("Rendu\\imageCoupe\\","")
    misc.imsave(name,edges_v)
#    plt.savefig(name)
#    plt.show()
    
    return [edges_v,name]
    
    
#---------- Tests ----------#
if __name__ == "__main__":
    # Début du traitement
    tic = time.time()
    
    url = "Test_bois_hv/Cimalmotto 10 a.jpg"
    M = img_gray(url)
    #M = img_gray('Les Fonds sous Chef-Lieu - annexe.jpg')
    #M = img_gray('Les Saugeais des Pémonts 3.jpg')
    #M = img_gray('Cimalmotto 6 a.jpg')
    
    sobel(M, url)
    sobel_h(M, url)
    sobel_v(M, url)
    
    # Fin du traitement
    toc = time.time()
    print ('%.3f sec elapsed ' % (toc-tic))