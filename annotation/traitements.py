# -*- coding: utf-8 -*-

import contours_sobel3 as cs2
import bois_hv_major as bhv

def traitements (img):
    # Ouverture de l'image en B&W
    M = cs2.img_gray(img)
    # Génération des contours
    img_h_prov = cs2.sobel_h(M, img)
    img_h = img_h_prov[0]
    img_v_prov = cs2.sobel_v(M, img)
    img_v = img_v_prov[0]
    #recupération du nom des images issues de sobel
    sobel_h_prov = cs2.sobel_h(M, img)
    sobel_h = sobel_h_prov[1].split('\\')
    sobel_v_prov = cs2.sobel_v(M, img)
    sobel_v = sobel_v_prov[1].split('\\')
    # Nombre de pixels des contours
    pxc_h = bhv.nb_pixels_contours(img_h)
    pxc_v = bhv.nb_pixels_contours(img_v)
    # Détermination des contours majoritaires
    maj = bhv.bois_major(pxc_h, pxc_v)
    
    liste = [sobel_h[len(sobel_h)-1], sobel_v[len(sobel_v)-1], str(pxc_h), str(pxc_v), maj]
    return liste

#traitements("Test_bois_hv/Cimalmotto 10 a.jpg")